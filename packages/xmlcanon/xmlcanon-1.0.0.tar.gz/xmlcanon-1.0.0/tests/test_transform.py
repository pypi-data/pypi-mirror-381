"""
Тесты для модуля ExcC14N трансформации
Проверка корректности работы согласно спецификации W3C
"""

import unittest
import sys
import os

# Добавляем путь к модулю для импорта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from xmlcanon import XmlCanonicalizer, canonicalize_xml
from xmlcanon.exceptions import InvalidXMLError, TransformationError


class TestXmlCanonicalizer(unittest.TestCase):
    """Тесты для XmlCanonicalizer"""

    def setUp(self):
        """Инициализация для каждого теста"""
        self.canonicalizer = XmlCanonicalizer()

    def test_simple_element(self):
        """Тест простого элемента без пространств имен"""
        xml_input = '<root>content</root>'
        expected = '<root>content</root>'
        result = self.canonicalizer.transform(xml_input)
        self.assertEqual(result, expected)

    def test_element_with_attributes(self):
        """Тест элемента с атрибутами"""
        xml_input = '<root attr2="value2" attr1="value1">content</root>'
        # Атрибуты должны быть отсортированы по алфавиту
        expected = '<root attr1="value1" attr2="value2">content</root>'
        result = self.canonicalizer.transform(xml_input)
        self.assertEqual(result, expected)

    def test_namespace_declarations(self):
        """Тест объявлений пространств имен"""
        xml_input = '''<root xmlns="http://default.com" xmlns:ns1="http://ns1.com">
            <ns1:child>content</ns1:child>
        </root>'''

        result = self.canonicalizer.transform(xml_input)

        # Проверяем что объявления пространств имен присутствуют
        self.assertIn('xmlns="http://default.com"', result)
        self.assertIn('xmlns:ns1="http://ns1.com"', result)
        self.assertIn('<ns1:child>', result)

    def test_unused_namespace_exclusion(self):
        """Тест исключения неиспользуемых пространств имен"""
        xml_input = '''<root xmlns:unused="http://unused.com" xmlns:used="http://used.com">
            <used:child>content</used:child>
        </root>'''

        result = self.canonicalizer.transform(xml_input)

        # Неиспользуемое пространство имен не должно присутствовать
        self.assertNotIn('xmlns:unused="http://unused.com"', result)
        # Используемое должно присутствовать
        self.assertIn('xmlns:used="http://used.com"', result)

    def test_inclusive_namespaces(self):
        """Тест принудительного включения пространств имен"""
        xml_input = '''<root xmlns:forced="http://forced.com" xmlns:used="http://used.com">
            <used:child>content</used:child>
        </root>'''

        # Создаем канонизатор с принудительным включением
        canonicalizer = XmlCanonicalizer(inclusive_ns_prefixes=['forced'])
        result = canonicalizer.transform(xml_input)

        # Принудительно включаемое пространство должно присутствовать
        self.assertIn('xmlns:forced="http://forced.com"', result)
        self.assertIn('xmlns:used="http://used.com"', result)

    def test_attribute_sorting(self):
        """Тест сортировки атрибутов"""
        xml_input = '''<root xmlns:ns2="http://ns2.com" xmlns:ns1="http://ns1.com"
                             ns2:attr="val2" regular="val" ns1:attr="val1">content</root>'''

        result = self.canonicalizer.transform(xml_input)

        # Находим порядок атрибутов в результате
        # Должны быть: сначала объявления ns, затем атрибуты с ns, затем обычные
        ns1_pos = result.find('xmlns:ns1=')
        ns2_pos = result.find('xmlns:ns2=')
        ns1_attr_pos = result.find('ns1:attr=')
        ns2_attr_pos = result.find('ns2:attr=')
        regular_pos = result.find('regular=')

        # Проверяем правильный порядок
        self.assertTrue(ns1_pos < ns2_pos)  # xmlns объявления отсортированы
        self.assertTrue(ns1_attr_pos < ns2_attr_pos)  # ns атрибуты отсортированы

    def test_text_normalization(self):
        """Тест нормализации текста"""
        xml_input = '<root>Text with &lt; and &amp; and &gt;</root>'
        result = self.canonicalizer.transform(xml_input)

        # Текст должен остаться экранированным
        self.assertIn('&lt;', result)
        self.assertIn('&amp;', result)
        self.assertIn('&gt;', result)

    def test_attribute_value_escaping(self):
        """Тест экранирования значений атрибутов"""
        xml_input = '<root attr="value with &quot; and &lt;">content</root>'
        result = self.canonicalizer.transform(xml_input)

        # Значение атрибута должно быть правильно экранировано
        self.assertIn('&quot;', result)
        self.assertIn('&lt;', result)

    def test_nested_elements(self):
        """Тест вложенных элементов"""
        xml_input = '''<root>
            <parent>
                <child>content</child>
            </parent>
        </root>'''

        result = self.canonicalizer.transform(xml_input)

        # Проверяем наличие всех элементов
        self.assertIn('<root>', result)
        self.assertIn('<parent>', result)
        self.assertIn('<child>content</child>', result)
        self.assertIn('</parent>', result)
        self.assertIn('</root>', result)

    def test_default_namespace_handling(self):
        """Тест обработки пространства имен по умолчанию"""
        xml_input = '<root xmlns="http://default.com"><child>content</child></root>'
        result = self.canonicalizer.transform(xml_input)

        # Пространство имен по умолчанию должно присутствовать
        self.assertIn('xmlns="http://default.com"', result)

    def test_invalid_xml(self):
        """Тест обработки некорректного XML"""
        invalid_xml = '<root><unclosed>'

        with self.assertRaises((InvalidXMLError, TransformationError)):
            self.canonicalizer.transform(invalid_xml)

    def test_convenience_function(self):
        """Тест удобной функции canonicalize_xml"""
        xml_input = '<root xmlns:ns="http://ns.com"><ns:child>content</ns:child></root>'
        result = canonicalize_xml(xml_input)

        self.assertIn('<root', result)
        self.assertIn('xmlns:ns="http://ns.com"', result)
        self.assertIn('<ns:child>content</ns:child>', result)


class TestRealWorldExamples(unittest.TestCase):
    """Тесты на реальных примерах XML"""

    def test_soap_envelope_structure(self):
        """Тест структуры SOAP конверта (подобной примеру из проекта)"""
        xml_input = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                                         xmlns:ns="urn://xsd.dmdk.goznak.ru/exchange/1.0">
            <soapenv:Header/>
            <soapenv:Body>
                <ns:SendDealRequest>
                    <ns:RequestData id="body">
                        <content>test</content>
                    </ns:RequestData>
                </ns:SendDealRequest>
            </soapenv:Body>
        </soapenv:Envelope>'''

        canonicalizer = XmlCanonicalizer()
        result = canonicalizer.transform(xml_input)

        # Проверяем корректность трансформации
        self.assertIn('xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"', result)
        self.assertIn('xmlns:ns="urn://xsd.dmdk.goznak.ru/exchange/1.0"', result)
        self.assertIn('<soapenv:Envelope', result)
        self.assertIn('<ns:SendDealRequest>', result)
        self.assertIn('id="body"', result)

    def test_signature_reference_element(self):
        """Тест элемента Reference из XML подписи"""
        xml_input = '''<Reference xmlns="http://www.w3.org/2000/09/xmldsig#" URI="#body">
            <Transforms>
                <Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
                <Transform Algorithm="urn://smev-gov-ru/xmldsig/transform"/>
            </Transforms>
            <DigestMethod Algorithm="urn:ietf:params:xml:ns:cpxmlsec:algorithms:gostr34112012-256"/>
        </Reference>'''

        result = canonicalize_xml(xml_input)

        # Проверяем что все атрибуты и элементы на месте
        self.assertIn('URI="#body"', result)
        self.assertIn('Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"', result)
        self.assertIn('Algorithm="urn://smev-gov-ru/xmldsig/transform"', result)


if __name__ == '__main__':
    # Запуск всех тестов
    unittest.main(verbosity=2)