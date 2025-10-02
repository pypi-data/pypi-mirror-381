"""
xmlcanon - XML Canonicalization для Python

Реализация трансформации Exclusive XML Canonicalization согласно спецификации W3C
для использования в XML подписях по стандарту ГОСТ.

Основные компоненты:
- XmlCanonicalizer: основной класс для канонизации XML
- canonicalize_xml: удобная функция для быстрого использования

Пример использования:
    from xmlcanon import canonicalize_xml

    xml_input = '<root xmlns:ns="http://example.com"><ns:element>text</ns:element></root>'
    canonicalized = canonicalize_xml(xml_input)
    print(canonicalized)
"""

from .transform import XmlCanonicalizer, canonicalize_xml
from .exceptions import XmlCanonError, InvalidXMLError, TransformationError

__version__ = "1.0.0"
__author__ = "Daniil (imdeniil)"
__email__ = "keemor821@gmail.com"
__license__ = "MIT"

__all__ = [
    "XmlCanonicalizer",
    "canonicalize_xml",
    "XmlCanonError",
    "InvalidXMLError",
    "TransformationError"
]