"""
Exclusive XML Canonicalization Transform (ExcC14N)
Реализация трансформации XML согласно спецификации W3C Exclusive XML Canonicalization
https://www.w3.org/2001/10/xml-exc-c14n#

Основано на анализе GostCryptography библиотеки для создания аналогичной функциональности на Python.
"""

import xml.etree.ElementTree as ET
from typing import List, Optional, Set, Dict, Tuple
from collections import OrderedDict
import re

from .exceptions import InvalidXMLError, TransformationError


class XmlCanonicalizer:
    """
    Реализация Exclusive XML Canonicalization Transform

    Exclusive C14N отличается от стандартной канонизации тем, что:
    - Исключает неиспользуемые объявления пространств имен
    - Обрабатывает только те пространства имен, которые визуально используются
    - Применяется для XML подписей, где важна точность и минимальность
    """

    def __init__(self, inclusive_ns_prefixes: Optional[List[str]] = None):
        """
        Инициализация трансформации

        Args:
            inclusive_ns_prefixes: Список префиксов пространств имен, которые должны
                                 быть включены в результат даже если не используются
        """
        self.inclusive_ns_prefixes = set(inclusive_ns_prefixes or [])

    def transform(self, xml_input: str) -> str:
        """
        Применить трансформацию ExcC14N к XML документу

        Args:
            xml_input: Исходный XML в виде строки

        Returns:
            Канонизированный XML

        Raises:
            InvalidXMLError: Если входной XML некорректен
            TransformationError: Если произошла ошибка при трансформации
        """
        try:
            # Используем lxml для лучшей обработки пространств имен
            try:
                from lxml import etree as lxml_etree
                # Парсим с сохранением пространств имен
                parser = lxml_etree.XMLParser(ns_clean=False, recover=False)
                root = lxml_etree.fromstring(xml_input.encode('utf-8'), parser)

                # Применяем канонизацию
                canonicalized = self._canonicalize_lxml_element(root, {}, set())
                return canonicalized

            except ImportError:
                # Fallback на стандартную библиотеку
                # Предварительно извлекаем пространства имен из строки
                ns_context = self._extract_namespaces_from_string(xml_input)
                root = ET.fromstring(xml_input)

                # Применяем канонизацию
                canonicalized = self._canonicalize_element(root, ns_context, set())
                return canonicalized

        except ET.ParseError as e:
            raise InvalidXMLError(f"Некорректный XML: {e}")
        except Exception as e:
            raise TransformationError(f"Ошибка трансформации: {e}")

    def _canonicalize_element(self, element: ET.Element,
                            inherited_ns: Dict[str, str],
                            inclusive_ns: Set[str]) -> str:
        """
        Рекурсивная канонизация XML элемента

        Args:
            element: Текущий элемент для канонизации
            inherited_ns: Унаследованные пространства имен
            inclusive_ns: Пространства имен для включения

        Returns:
            Канонизированное представление элемента
        """
        result = []

        # Определяем текущие пространства имен
        current_ns = inherited_ns.copy()
        element_ns = self._extract_namespaces(element)

        # Обновляем текущие пространства имен
        for prefix, uri in element_ns.items():
            current_ns[prefix] = uri

        # Получаем имя элемента с учетом пространства имен
        tag_name = self._get_qualified_name(element.tag, current_ns)

        # Начинаем открывающий тег
        result.append(f"<{tag_name}")

        # Добавляем объявления пространств имен
        ns_declarations = self._get_namespace_declarations(
            element, inherited_ns, inclusive_ns
        )
        for ns_decl in sorted(ns_declarations):
            result.append(f" {ns_decl}")

        # Добавляем атрибуты
        attributes = self._get_sorted_attributes(element, current_ns)
        for attr in attributes:
            result.append(f" {attr}")

        # Закрываем открывающий тег
        result.append(">")

        # Обрабатываем содержимое
        text_content = self._normalize_text(element.text)
        if text_content:
            result.append(text_content)

        # Рекурсивно обрабатываем дочерние элементы
        for child in element:
            child_inclusive_ns = self._get_visibly_used_ns(child, current_ns)
            child_canonical = self._canonicalize_element(
                child, current_ns, child_inclusive_ns
            )
            result.append(child_canonical)

            # Добавляем текст после дочернего элемента
            tail_content = self._normalize_text(child.tail)
            if tail_content:
                result.append(tail_content)

        # Закрывающий тег
        result.append(f"</{tag_name}>")

        return "".join(result)

    def _extract_namespaces(self, element: ET.Element) -> Dict[str, str]:
        """
        Извлекает объявления пространств имен из элемента

        Args:
            element: XML элемент

        Returns:
            Словарь префикс -> URI пространства имен
        """
        namespaces = {}

        # Обрабатываем атрибуты xmlns
        for key, value in element.attrib.items():
            if key == "xmlns":
                # Пространство имен по умолчанию
                namespaces[""] = value
            elif key.startswith("xmlns:"):
                # Именованное пространство имен
                prefix = key[6:]  # Убираем "xmlns:"
                namespaces[prefix] = value

        return namespaces

    def _get_qualified_name(self, tag: str, namespaces: Dict[str, str]) -> str:
        """
        Получает квалифицированное имя элемента с учетом пространств имен

        Args:
            tag: Имя тега (может содержать {namespace}localname)
            namespaces: Текущие пространства имен

        Returns:
            Квалифицированное имя
        """
        # Если тег содержит namespace в формате {uri}localname
        if tag.startswith("{"):
            end_brace = tag.find("}")
            namespace_uri = tag[1:end_brace]
            local_name = tag[end_brace + 1:]

            # Ищем соответствующий префикс
            for prefix, uri in namespaces.items():
                if uri == namespace_uri:
                    if prefix == "":
                        return local_name
                    else:
                        return f"{prefix}:{local_name}"

            # Если префикс не найден, возвращаем локальное имя
            return local_name

        return tag

    def _get_namespace_declarations(self, element: ET.Element,
                                  inherited_ns: Dict[str, str],
                                  inclusive_ns: Set[str]) -> List[str]:
        """
        Получает объявления пространств имен для элемента

        Args:
            element: XML элемент
            inherited_ns: Унаследованные пространства имен
            inclusive_ns: Пространства имен для включения

        Returns:
            Список строк объявлений пространств имен
        """
        declarations = []
        current_ns = self._extract_namespaces(element)

        # Определяем видимо используемые пространства имен
        visibly_used = self._get_visibly_used_ns(element,
                                                {**inherited_ns, **current_ns})

        # Добавляем принудительно включаемые пространства имен
        visibly_used.update(self.inclusive_ns_prefixes)
        visibly_used.update(inclusive_ns)

        for prefix, uri in current_ns.items():
            # Включаем объявление если:
            # - Пространство имен видимо используется
            # - Или оно отличается от унаследованного
            should_include = (
                prefix in visibly_used or
                inherited_ns.get(prefix) != uri
            )

            if should_include:
                if prefix == "":
                    declarations.append(f'xmlns="{self._escape_attribute_value(uri)}"')
                else:
                    declarations.append(f'xmlns:{prefix}="{self._escape_attribute_value(uri)}"')

        return declarations

    def _get_visibly_used_ns(self, element: ET.Element,
                           namespaces: Dict[str, str]) -> Set[str]:
        """
        Определяет видимо используемые пространства имен в элементе

        Args:
            element: XML элемент
            namespaces: Доступные пространства имен

        Returns:
            Множество префиксов видимо используемых пространств имен
        """
        used_ns = set()

        # Проверяем пространство имен самого элемента
        if element.tag.startswith("{"):
            end_brace = element.tag.find("}")
            namespace_uri = element.tag[1:end_brace]

            for prefix, uri in namespaces.items():
                if uri == namespace_uri:
                    used_ns.add(prefix)
                    break

        # Проверяем атрибуты
        for attr_name in element.attrib:
            if ":" in attr_name and not attr_name.startswith("xmlns"):
                prefix = attr_name.split(":")[0]
                if prefix in namespaces:
                    used_ns.add(prefix)

        return used_ns

    def _get_sorted_attributes(self, element: ET.Element,
                             namespaces: Dict[str, str]) -> List[str]:
        """
        Получает отсортированный список атрибутов элемента

        Args:
            element: XML элемент
            namespaces: Текущие пространства имен

        Returns:
            Список отсортированных атрибутов в канонической форме
        """
        attributes = []

        for name, value in element.attrib.items():
            # Пропускаем объявления пространств имен (они обрабатываются отдельно)
            if name == "xmlns" or name.startswith("xmlns:"):
                continue

            # Получаем канонический вид атрибута
            canonical_name = self._get_canonical_attribute_name(name, namespaces)
            escaped_value = self._escape_attribute_value(value)
            attributes.append(f'{canonical_name}="{escaped_value}"')

        # Сортируем атрибуты
        # Сначала атрибуты без пространства имен, затем с пространством имен
        def sort_key(attr: str) -> Tuple[int, str, str]:
            attr_name = attr.split("=")[0]
            if ":" in attr_name:
                prefix, local = attr_name.split(":", 1)
                namespace_uri = namespaces.get(prefix, "")
                return (0, namespace_uri, local)
            else:
                return (1, "", attr_name)

        return sorted(attributes, key=sort_key)

    def _get_canonical_attribute_name(self, name: str,
                                    namespaces: Dict[str, str]) -> str:
        """
        Получает каноническое имя атрибута

        Args:
            name: Имя атрибута
            namespaces: Текущие пространства имен

        Returns:
            Каноническое имя атрибута
        """
        if ":" in name:
            prefix, local_name = name.split(":", 1)
            if prefix in namespaces:
                return f"{prefix}:{local_name}"

        return name

    def _normalize_text(self, text: Optional[str]) -> str:
        """
        Нормализует текстовое содержимое согласно правилам C14N

        Args:
            text: Исходный текст

        Returns:
            Нормализованный текст
        """
        if not text:
            return ""

        # Заменяем символы согласно правилам C14N
        normalized = text.replace("&", "&amp;")
        normalized = normalized.replace("<", "&lt;")
        normalized = normalized.replace(">", "&gt;")
        normalized = normalized.replace("\r\n", "\n")
        normalized = normalized.replace("\r", "\n")

        return normalized

    def _escape_attribute_value(self, value: str) -> str:
        """
        Экранирует значение атрибута согласно правилам C14N

        Args:
            value: Исходное значение атрибута

        Returns:
            Экранированное значение
        """
        escaped = value.replace("&", "&amp;")
        escaped = escaped.replace("<", "&lt;")
        escaped = escaped.replace('"', "&quot;")
        escaped = escaped.replace("\t", "&#9;")
        escaped = escaped.replace("\n", "&#10;")
        escaped = escaped.replace("\r", "&#13;")

        return escaped

    def _extract_namespaces_from_string(self, xml_string: str) -> Dict[str, str]:
        """
        Извлекает объявления пространств имен из XML строки с помощью регулярных выражений
        Это fallback метод для случаев когда lxml недоступна
        """
        import re
        namespaces = {}

        # Ищем объявления xmlns
        xmlns_pattern = r'xmlns(?::(\w+))?="([^"]*)"'
        matches = re.findall(xmlns_pattern, xml_string)

        for prefix, uri in matches:
            if prefix:
                namespaces[prefix] = uri
            else:
                namespaces[""] = uri

        return namespaces

    def _canonicalize_lxml_element(self, element, inherited_ns: Dict[str, str], inclusive_ns: Set[str]) -> str:
        """
        Канонизация элемента с использованием lxml (более точная обработка пространств имен)
        """
        try:
            from lxml import etree
        except ImportError:
            # Если lxml недоступна, используем стандартный метод
            return self._canonicalize_element(element, inherited_ns, inclusive_ns)

        result = []

        # Получаем информацию об элементе
        tag = element.tag
        text = element.text
        tail = element.tail
        attrib = element.attrib

        # Обрабатываем пространства имен
        current_ns = inherited_ns.copy()

        # Получаем пространства имен элемента
        element_nsmap = element.nsmap if hasattr(element, 'nsmap') else {}
        for prefix, uri in element_nsmap.items():
            if prefix is None:
                current_ns[""] = uri
            else:
                current_ns[prefix] = uri

        # Получаем имя тега
        if isinstance(tag, str):
            if tag.startswith('{'):
                # Формат {namespace}localname
                ns_end = tag.find('}')
                namespace_uri = tag[1:ns_end]
                local_name = tag[ns_end + 1:]

                # Находим префикс для этого namespace
                tag_prefix = None
                for prefix, uri in current_ns.items():
                    if uri == namespace_uri:
                        tag_prefix = prefix
                        break

                if tag_prefix and tag_prefix != "":
                    qualified_name = f"{tag_prefix}:{local_name}"
                else:
                    qualified_name = local_name
            else:
                qualified_name = tag
        else:
            qualified_name = str(tag)

        # Начинаем тег
        result.append(f"<{qualified_name}")

        # Добавляем объявления пространств имен
        used_namespaces = self._get_visibly_used_ns_lxml(element, current_ns)
        used_namespaces.update(self.inclusive_ns_prefixes)
        used_namespaces.update(inclusive_ns)

        # Сортируем и добавляем объявления пространств имен
        ns_declarations = []
        for prefix, uri in sorted(current_ns.items()):
            # Объявляем только если:
            # 1. Пространство имен видимо используется в этом элементе или его дочерних
            # 2. И это новое/измененное объявление по сравнению с унаследованным
            should_declare = (
                (prefix in used_namespaces or prefix in inclusive_ns) and
                inherited_ns.get(prefix) != uri
            )

            if should_declare:
                if prefix == "":
                    ns_declarations.append(f'xmlns="{self._escape_attribute_value(uri)}"')
                else:
                    ns_declarations.append(f'xmlns:{prefix}="{self._escape_attribute_value(uri)}"')

        for decl in ns_declarations:
            result.append(f" {decl}")

        # Добавляем атрибуты (исключая xmlns)
        sorted_attrs = []
        for name, value in attrib.items():
            if not (name == 'xmlns' or name.startswith('xmlns:')):
                # Обрабатываем имя атрибута
                if isinstance(name, str) and name.startswith('{'):
                    # Формат {namespace}localname
                    ns_end = name.find('}')
                    namespace_uri = name[1:ns_end]
                    local_name = name[ns_end + 1:]

                    # Находим префикс
                    attr_prefix = None
                    for prefix, uri in current_ns.items():
                        if uri == namespace_uri:
                            attr_prefix = prefix
                            break

                    if attr_prefix and attr_prefix != "":
                        attr_name = f"{attr_prefix}:{local_name}"
                    else:
                        attr_name = local_name
                else:
                    attr_name = name

                sorted_attrs.append((attr_name, value))

        # Сортируем атрибуты
        sorted_attrs.sort(key=lambda x: (0 if ':' not in x[0] else 1, x[0]))

        for attr_name, attr_value in sorted_attrs:
            escaped_value = self._escape_attribute_value(attr_value)
            result.append(f' {attr_name}="{escaped_value}"')

        result.append(">")

        # Добавляем текст
        if text:
            normalized_text = self._normalize_text(text)
            if normalized_text:
                result.append(normalized_text)

        # Обрабатываем дочерние элементы
        for child in element:
            child_canonical = self._canonicalize_lxml_element(child, current_ns, set())
            result.append(child_canonical)

            if child.tail:
                normalized_tail = self._normalize_text(child.tail)
                if normalized_tail:
                    result.append(normalized_tail)

        # Закрывающий тег
        result.append(f"</{qualified_name}>")

        return "".join(result)

    def _get_visibly_used_ns_lxml(self, element, namespaces: Dict[str, str]) -> Set[str]:
        """
        Определяет видимо используемые пространства имен в lxml элементе
        """
        used_ns = set()

        # Проверяем пространство имен самого элемента
        if isinstance(element.tag, str) and element.tag.startswith('{'):
            ns_end = element.tag.find('}')
            namespace_uri = element.tag[1:ns_end]

            for prefix, uri in namespaces.items():
                if uri == namespace_uri:
                    used_ns.add(prefix)
                    break

        # Проверяем атрибуты элемента
        if element.attrib:
            for name in element.attrib:
                if isinstance(name, str) and name.startswith('{'):
                    # Атрибут с пространством имен в формате {uri}localname
                    ns_end = name.find('}')
                    namespace_uri = name[1:ns_end]

                    for prefix, uri in namespaces.items():
                        if uri == namespace_uri:
                            used_ns.add(prefix)
                            break
                elif ':' in name and not name.startswith('xmlns'):
                    # Атрибут с префиксом
                    prefix = name.split(':')[0]
                    if prefix in namespaces:
                        used_ns.add(prefix)

        # Рекурсивно проверяем дочерние элементы
        for child in element:
            child_used = self._get_visibly_used_ns_lxml(child, namespaces)
            used_ns.update(child_used)

        return used_ns


def canonicalize_xml(xml_input: str,
                     inclusive_ns_prefixes: Optional[List[str]] = None) -> str:
    """
    Удобная функция для канонизации XML

    Args:
        xml_input: Исходный XML
        inclusive_ns_prefixes: Префиксы пространств имен для принудительного включения

    Returns:
        Канонизированный XML

    Raises:
        InvalidXMLError: Если входной XML некорректен
        TransformationError: Если произошла ошибка при трансформации
    """
    canonicalizer = XmlCanonicalizer(inclusive_ns_prefixes)
    return canonicalizer.transform(xml_input)