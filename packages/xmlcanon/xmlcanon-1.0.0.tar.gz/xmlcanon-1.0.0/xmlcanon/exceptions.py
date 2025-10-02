"""
Исключения для модуля xmlcanon
"""


class XmlCanonError(Exception):
    """Базовое исключение для ошибок XML канонизации"""
    pass


class InvalidXMLError(XmlCanonError):
    """Исключение для некорректного XML"""
    pass


class TransformationError(XmlCanonError):
    """Исключение для ошибок канонизации"""
    pass


class NamespaceError(XmlCanonError):
    """Исключение для ошибок работы с пространствами имен"""
    pass