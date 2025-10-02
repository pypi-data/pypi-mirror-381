"""
Пример интеграции ExcC14N с ГОСТ подписями
Демонстрация использования в контексте XML подписей
"""

import sys
import os

# Добавляем путь к модулю
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from xmlcanon import canonicalize_xml


def prepare_xml_for_gost_signature():
    """
    Пример подготовки XML для создания ГОСТ подписи
    Демонстрирует первый шаг в процессе создания XML подписи
    """
    print("=== Подготовка XML для ГОСТ подписи ===")

    # Пример XML документа для подписания (подобно Test_Deal.xml из проекта)
    xml_document = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                                       xmlns:ns="urn://xsd.dmdk.goznak.ru/exchange/1.0"
                                       xmlns:ns1="urn://xsd.dmdk.goznak.ru/deal/1.0"
                                       xmlns:ns2="urn://xsd.dmdk.goznak.ru/contractor/1.0">
        <soapenv:Header/>
        <soapenv:Body>
            <ns:SendDealRequest>
                <ns:CallerSignature>
                    <!-- Здесь будет XML подпись -->
                </ns:CallerSignature>
                <ns:RequestData id="body">
                    <ns:deal>
                        <ns1:number>001-KTR578/5</ns1:number>
                        <ns1:dealDate>2021-04-14</ns1:dealDate>
                        <ns1:dealType>DL_SALE</ns1:dealType>
                        <ns1:provider>
                            <ns2:legal>
                                <ns2:OGRN>1135024004906</ns2:OGRN>
                                <ns2:KPP>502401001</ns2:KPP>
                            </ns2:legal>
                        </ns1:provider>
                        <ns1:currency>RUB</ns1:currency>
                        <ns1:amount>10000000000</ns1:amount>
                    </ns:deal>
                </ns:RequestData>
            </ns:SendDealRequest>
        </soapenv:Body>
    </soapenv:Envelope>'''

    print("Исходный XML документ:")
    print(xml_document)

    # Шаг 1: Применяем ExcC14N трансформацию
    print("\n--- Шаг 1: ExcC14N трансформация ---")
    canonicalized = canonicalize_xml(xml_document)
    print("Результат ExcC14N:")
    print(canonicalized)

    # Шаг 2: Здесь должна применяться СМЭВ трансформация
    print("\n--- Шаг 2: СМЭВ трансформация (требует отдельного модуля) ---")
    print("После ExcC14N должна применяться СМЭВ трансформация")
    print("URI: urn://smev-gov-ru/xmldsig/transform")

    # Шаг 3: Вычисление хеша ГОСТ
    print("\n--- Шаг 3: Вычисление хеша ГОСТ ---")
    print("Применить ГОСТ Р 34.11-2012 к результату СМЭВ трансформации")

    # Шаг 4: Создание подписи
    print("\n--- Шаг 4: Создание подписи ---")
    print("Подписать хеш с использованием ГОСТ Р 34.10-2012")

    return canonicalized


def simulate_signature_creation():
    """
    Симуляция процесса создания XML подписи
    """
    print("\n=== Симуляция создания XML подписи ===")

    # Элемент Reference, который будет подписываться
    reference_element = '''<Reference xmlns="http://www.w3.org/2000/09/xmldsig#" URI="#body">
        <Transforms>
            <Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
            <Transform Algorithm="urn://smev-gov-ru/xmldsig/transform"/>
        </Transforms>
        <DigestMethod Algorithm="urn:ietf:params:xml:ns:cpxmlsec:algorithms:gostr34112012-256"/>
        <DigestValue><!-- Здесь будет хеш --></DigestValue>
    </Reference>'''

    print("Reference элемент для подписи:")
    print(reference_element)

    # Применяем ExcC14N к Reference элементу
    canonicalized_ref = canonicalize_xml(reference_element)
    print("\nCanonical Reference:")
    print(canonicalized_ref)

    # Пример структуры итоговой подписи
    signature_structure = '''<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
        <ds:SignedInfo>
            <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
            <ds:SignatureMethod Algorithm="urn:ietf:params:xml:ns:cpxmlsec:algorithms:gostr34102012-gostr34112012-256"/>
            <!-- Reference элементы -->
        </ds:SignedInfo>
        <ds:SignatureValue><!-- ГОСТ подпись --></ds:SignatureValue>
        <ds:KeyInfo>
            <ds:X509Data>
                <ds:X509Certificate><!-- Сертификат --></ds:X509Certificate>
            </ds:X509Data>
        </ds:KeyInfo>
    </ds:Signature>'''

    print("\nСтруктура итоговой подписи:")
    print(signature_structure)


def demonstrate_namespace_handling():
    """
    Демонстрация особенностей обработки пространств имен для ГОСТ подписей
    """
    print("\n=== Обработка пространств имен для ГОСТ подписей ===")

    # XML с множественными пространствами имен
    complex_xml = '''<root xmlns="http://default.ns"
                          xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
                          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                          xmlns:gost="urn:ietf:params:xml:ns:cpxmlsec:algorithms">
        <data>
            <item xsi:type="string">Value1</item>
            <item xsi:type="string">Value2</item>
        </data>
        <ds:Signature>
            <ds:SignedInfo>
                <ds:SignatureMethod Algorithm="gost:gostr34102012-gostr34112012-256"/>
            </ds:SignedInfo>
        </ds:Signature>
    </root>'''

    print("XML с множественными пространствами имен:")
    print(complex_xml)

    result = canonicalize_xml(complex_xml)
    print("\nРезультат ExcC14N (неиспользуемые пространства исключены):")
    print(result)

    # Проверяем какие пространства имен остались
    remaining_ns = []
    if 'xmlns=' in result:
        remaining_ns.append('default')
    if 'xmlns:ds=' in result:
        remaining_ns.append('ds')
    if 'xmlns:xsi=' in result:
        remaining_ns.append('xsi')
    if 'xmlns:gost=' in result:
        remaining_ns.append('gost')

    print(f"\nОставшиеся пространства имен: {remaining_ns}")


if __name__ == "__main__":
    # Запуск всех примеров
    prepare_xml_for_gost_signature()
    simulate_signature_creation()
    demonstrate_namespace_handling()

    print("\n=== Интеграция с ГОСТ завершена ===")
    print("\nСледующие шаги для полной реализации:")
    print("1. Реализовать СМЭВ трансформацию")
    print("2. Интегрировать ГОСТ криптографию")
    print("3. Создать полный класс подписания XML")