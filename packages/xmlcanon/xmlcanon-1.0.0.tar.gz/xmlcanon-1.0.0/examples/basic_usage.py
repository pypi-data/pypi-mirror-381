"""
Базовые примеры использования модуля ExcC14N
"""

import sys
import os

# Добавляем путь к модулю
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from xmlcanon import canonicalize_xml, XmlCanonicalizer


def example_simple_usage():
    """Простой пример использования"""
    print("=== Простой пример использования ===")

    xml_input = '''<document xmlns="http://example.com"
                             xmlns:sig="http://www.w3.org/2000/09/xmldsig#">
        <content>Текстовое содержимое</content>
        <sig:signature>signature_data</sig:signature>
    </document>'''

    print("Исходный XML:")
    print(xml_input)
    print("\nРезультат ExcC14N трансформации:")

    result = canonicalize_xml(xml_input)
    print(result)


def example_namespace_exclusion():
    """Пример исключения неиспользуемых пространств имен"""
    print("\n=== Пример исключения неиспользуемых пространств имен ===")

    xml_input = '''<root xmlns:used="http://used.ns"
                        xmlns:unused="http://unused.ns">
        <used:element attribute="value">
            <content>Only 'used' namespace is actually used</content>
        </used:element>
    </root>'''

    print("Исходный XML (с неиспользуемыми пространствами имен):")
    print(xml_input)

    result = canonicalize_xml(xml_input)
    print("\nРезультат (неиспользуемые пространства имен исключены):")
    print(result)

    # Проверим что неиспользуемые пространства действительно исключены
    unused_excluded = 'xmlns:unused' not in result
    used_included = 'xmlns:used' in result

    print(f"\nПроверка:")
    print(f"  unused исключено: {unused_excluded}")
    print(f"  used включено: {used_included}")


def example_inclusive_namespaces():
    """Пример принудительного включения пространств имен"""
    print("\n=== Пример принудительного включения пространств имен ===")

    xml_input = '''<root xmlns:force="http://force.ns"
                        xmlns:used="http://used.ns">
        <used:element>Only used namespace is actually used</used:element>
    </root>'''

    print("Исходный XML:")
    print(xml_input)

    # Обычная трансформация
    result_normal = canonicalize_xml(xml_input)
    print("\nОбычная трансформация (force исключено):")
    print(result_normal)

    # Канонизация с принудительным включением
    canonicalizer = XmlCanonicalizer(inclusive_ns_prefixes=['force'])
    result_inclusive = canonicalizer.transform(xml_input)
    print("\nС принудительным включением 'force':")
    print(result_inclusive)


def example_soap_structure():
    """Пример SOAP структуры подобной ГИИС ДМДК"""
    print("\n=== Пример SOAP-подобной структуры ===")

    xml_input = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                                    xmlns:ns="urn://xsd.dmdk.goznak.ru/exchange/1.0">
        <soapenv:Header/>
        <soapenv:Body>
            <ns:SendDealRequest>
                <ns:CallerSignature>
                    <!-- Здесь будет подпись -->
                </ns:CallerSignature>
                <ns:RequestData id="body">
                    <ns:deal>
                        <number>001-KTR578/5</number>
                        <dealDate>2021-04-14</dealDate>
                    </ns:deal>
                </ns:RequestData>
            </ns:SendDealRequest>
        </soapenv:Body>
    </soapenv:Envelope>'''

    print("SOAP-подобная структура:")
    print(xml_input)

    result = canonicalize_xml(xml_input)
    print("\nРезультат ExcC14N трансформации:")
    print(result)


def example_attribute_sorting():
    """Пример сортировки атрибутов"""
    print("\n=== Пример сортировки атрибутов ===")

    xml_input = '''<element xmlns:z="http://z.ns"
                           xmlns:a="http://a.ns"
                           z:attr="z_value"
                           regular="regular_value"
                           a:attr="a_value">
        <a:child/>
        <z:child/>
    </element>'''

    print("Исходный XML (атрибуты в произвольном порядке):")
    print(xml_input)

    result = canonicalize_xml(xml_input)
    print("\nРезультат (атрибуты отсортированы):")
    print(result)


if __name__ == "__main__":
    # Запуск всех примеров
    example_simple_usage()
    example_namespace_exclusion()
    example_inclusive_namespaces()
    example_soap_structure()
    example_attribute_sorting()

    print("\n=== Все примеры выполнены ===")
    print("\nДля использования в вашем коде:")
    print("from xmlcanon import canonicalize_xml")
    print("result = canonicalize_xml(your_xml)")