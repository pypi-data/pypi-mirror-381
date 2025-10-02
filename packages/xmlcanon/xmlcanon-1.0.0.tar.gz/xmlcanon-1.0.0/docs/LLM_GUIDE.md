# xmlcanon - Quick Start Guide for LLMs

**Библиотека для канонизации XML** согласно спецификации W3C Exclusive XML Canonicalization (ExcC14N).

---

## 🚀 Установка

```bash
pip install xmlcanon
```

**С lxml (рекомендуется для лучшей производительности):**
```bash
pip install xmlcanon[lxml]
```

---

## 📦 Импорт

```python
from xmlcanon import canonicalize_xml, XmlCanonicalizer
from xmlcanon.exceptions import InvalidXMLError, TransformationError
```

---

## ⚡ Базовое использование (90% случаев)

### Простая канонизация XML

```python
from xmlcanon import canonicalize_xml

xml_input = '''<root xmlns:ns="http://example.com">
    <ns:element attr="value">Content</ns:element>
</root>'''

# Канонизировать XML
result = canonicalize_xml(xml_input)
print(result)
```

**Выход:**
```xml
<root xmlns:ns="http://example.com"><ns:element attr="value">Content</ns:element></root>
```

---

## 🔧 Расширенное использование

### Принудительное включение пространств имен

Иногда нужно включить пространство имен, даже если оно не используется:

```python
from xmlcanon import XmlCanonicalizer

xml_input = '''<root xmlns:force="http://force.com" xmlns:used="http://used.com">
    <used:element>Only used namespace is actually used</used:element>
</root>'''

# Создать канонизатор с принудительным включением namespace
canonicalizer = XmlCanonicalizer(inclusive_ns_prefixes=['force'])
result = canonicalizer.transform(xml_input)
```

**Результат:** `xmlns:force` будет включено, несмотря на то что не используется в XML.

---

## 🎯 Типичные сценарии использования

### 1. Подготовка XML для подписи (ГОСТ, XML-DSig)

```python
from xmlcanon import canonicalize_xml

# Шаг 1: Канонизировать XML перед подписанием
xml_data = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
    <soapenv:Body>
        <ns:Request xmlns:ns="http://example.com" id="body">
            <data>Important data</data>
        </ns:Request>
    </soapenv:Body>
</soapenv:Envelope>'''

canonicalized = canonicalize_xml(xml_data)

# Шаг 2: Теперь можно применить другие трансформации или вычислить хеш
# hash_value = compute_hash(canonicalized)
```

### 2. Очистка XML от неиспользуемых namespace

```python
from xmlcanon import canonicalize_xml

messy_xml = '''<root xmlns:unused1="http://a.com"
                     xmlns:unused2="http://b.com"
                     xmlns:used="http://c.com">
    <used:element>Only this namespace is used</used:element>
</root>'''

# Автоматически удалит unused1 и unused2
clean_xml = canonicalize_xml(messy_xml)
```

### 3. Нормализация XML для сравнения

```python
from xmlcanon import canonicalize_xml

xml1 = '<root attr2="b" attr1="a"><child/></root>'
xml2 = '<root attr1="a" attr2="b">\n    <child/>\n</root>'

# Оба XML станут идентичными после канонизации
canonical1 = canonicalize_xml(xml1)
canonical2 = canonicalize_xml(xml2)

assert canonical1 == canonical2  # True
```

---

## ⚠️ Обработка ошибок

```python
from xmlcanon import canonicalize_xml
from xmlcanon.exceptions import InvalidXMLError, TransformationError

try:
    result = canonicalize_xml(invalid_xml)
except InvalidXMLError as e:
    print(f"XML некорректен: {e}")
except TransformationError as e:
    print(f"Ошибка канонизации: {e}")
```

---

## 📚 API Reference

### `canonicalize_xml(xml_input, inclusive_ns_prefixes=None)`

**Параметры:**
- `xml_input` (str): XML строка для канонизации
- `inclusive_ns_prefixes` (List[str], optional): Префиксы namespace для принудительного включения

**Возвращает:** `str` - Канонизированный XML

**Исключения:**
- `InvalidXMLError` - Некорректный XML
- `TransformationError` - Ошибка при канонизации

### `XmlCanonicalizer(inclusive_ns_prefixes=None)`

**Класс для многократного использования канонизации с одинаковыми настройками.**

**Методы:**
- `transform(xml_input: str) -> str` - Канонизировать XML

**Пример:**
```python
from xmlcanon import XmlCanonicalizer

# Создать один раз
canonicalizer = XmlCanonicalizer(inclusive_ns_prefixes=['ds', 'xsi'])

# Использовать многократно
result1 = canonicalizer.transform(xml1)
result2 = canonicalizer.transform(xml2)
result3 = canonicalizer.transform(xml3)
```

---

## 🔍 Что делает канонизация?

1. **Удаляет лишние пробелы и переносы строк** между тегами
2. **Сортирует атрибуты** в определённом порядке
3. **Удаляет неиспользуемые namespace** (ключевая особенность ExcC14N)
4. **Нормализует экранирование** специальных символов
5. **Приводит к единому формату** для точного сравнения или хеширования

---

## 💡 Важные особенности

### Exclusive C14N vs обычная канонизация

**Exclusive C14N** (этот модуль):
- ❌ Удаляет неиспользуемые namespace объявления
- ✅ Идеален для XML подписей
- ✅ Меньший размер результата

**Обычная C14N:**
- ✅ Сохраняет все namespace объявления
- ❌ Больший размер результата

### Когда использовать `inclusive_ns_prefixes`?

Используйте когда:
- XML подпись требует определённые namespace в подписываемой части
- Спецификация явно требует включения определённых префиксов
- Нужно сохранить контекст namespace для вложенных элементов

**Пример из спецификации XML-DSig:**
```python
canonicalizer = XmlCanonicalizer(inclusive_ns_prefixes=['ds', 'xsi'])
```

---

## 📖 Примеры из реальной практики

### SOAP с XML подписью (ГИИС ДМДК)

```python
from xmlcanon import canonicalize_xml

soap_envelope = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                                     xmlns:ns="urn://xsd.dmdk.goznak.ru/exchange/1.0">
    <soapenv:Header/>
    <soapenv:Body>
        <ns:SendDealRequest>
            <ns:CallerSignature>
                <!-- Сюда вставляется XML подпись -->
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

# Шаг 1: Канонизация для подписи
canonical_xml = canonicalize_xml(soap_envelope)

# Шаг 2: Применить СМЭВ трансформацию (если требуется)
# smev_result = apply_smev_transform(canonical_xml)

# Шаг 3: Вычислить ГОСТ хеш
# digest = compute_gost_hash(smev_result)
```

### XML-DSig Reference элемент

```python
from xmlcanon import canonicalize_xml

reference = '''<Reference xmlns="http://www.w3.org/2000/09/xmldsig#" URI="#body">
    <Transforms>
        <Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
        <Transform Algorithm="urn://smev-gov-ru/xmldsig/transform"/>
    </Transforms>
    <DigestMethod Algorithm="urn:ietf:params:xml:ns:cpxmlsec:algorithms:gostr34112012-256"/>
    <DigestValue>BASE64_HASH_HERE</DigestValue>
</Reference>'''

canonical_ref = canonicalize_xml(reference)
# Используется для вычисления SignatureValue
```

---

## 🧪 Тестирование

Модуль содержит 14 unit-тестов:

```bash
# Запустить тесты
python -m pytest tests/

# С покрытием
python -m pytest tests/ --cov=xmlcanon --cov-report=html
```

**Примеры тестов:**
- Базовая канонизация элементов
- Исключение неиспользуемых namespace
- Принудительное включение namespace
- Сортировка атрибутов
- Экранирование спецсимволов
- SOAP структуры
- Обработка ошибок

---

## 🎓 Быстрая справка

| Задача | Код |
|--------|-----|
| Простая канонизация | `canonicalize_xml(xml_str)` |
| С принудительным namespace | `XmlCanonicalizer(inclusive_ns_prefixes=['ds']).transform(xml_str)` |
| Обработать ошибку | `try: ... except InvalidXMLError: ...` |
| Многократное использование | `canon = XmlCanonicalizer(); canon.transform(xml1)` |

---

## ❓ FAQ

**Q: Чем отличается от `lxml.etree.tostring(method='c14n')`?**
A: Это **Exclusive C14N** (удаляет неиспользуемые namespace), а не обычная C14N. Критично для XML подписей.

**Q: Нужен ли lxml?**
A: Опционально, но **рекомендуется** для лучшей производительности и точности.

**Q: Можно ли канонизировать часть XML?**
A: Да, передайте нужный фрагмент как строку.

**Q: Поддерживает ли комментарии?**
A: Согласно спецификации ExcC14N, комментарии удаляются по умолчанию.

**Q: Работает с кириллицей?**
A: Да, полная поддержка UTF-8.

---

## 🔗 Полезные ссылки

- **PyPI**: https://pypi.org/project/xmlcanon/
- **Репозиторий**: https://github.com/imdeniil/xmlcanon
- **Спецификация W3C**: https://www.w3.org/2001/10/xml-exc-c14n
- **XML-DSig**: https://www.w3.org/TR/xmldsig-core/

---

**Автор**: Daniil (imdeniil)
**Email**: keemor821@gmail.com
**Версия**: 1.0.0
**Лицензия**: MIT
