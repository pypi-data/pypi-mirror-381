"""
Тесты производительности модуля ExcC14N
"""

import sys
import os
import time
import statistics

# Добавляем путь к модулю
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from xmlcanon import canonicalize_xml, XmlCanonicalizer


def generate_test_xml(size="small"):
    """Генерирует тестовый XML различных размеров"""

    if size == "small":
        return '''<root xmlns:ns1="http://ns1.com" xmlns:ns2="http://ns2.com">
            <ns1:element attr="value">
                <content>Small test content</content>
            </ns1:element>
        </root>'''

    elif size == "medium":
        # Средний XML с множественными элементами
        elements = []
        for i in range(50):
            elements.append(f'''
            <ns{i%3}:item{i} xmlns:ns{i%3}="http://ns{i%3}.com" attr{i}="value{i}">
                <content>Content for item {i}</content>
                <details>
                    <info>Information {i}</info>
                    <data>Data {i}</data>
                </details>
            </ns{i%3}:item{i}>''')

        return f'''<root xmlns:ns0="http://ns0.com"
                        xmlns:ns1="http://ns1.com"
                        xmlns:ns2="http://ns2.com">
            {''.join(elements)}
        </root>'''

    elif size == "large":
        # Большой XML с вложенными структурами
        elements = []
        for i in range(200):
            nested = []
            for j in range(5):
                nested.append(f'''
                    <nested{j} xmlns:n{j}="http://nested{j}.com" n{j}:attr="val{j}">
                        <data>Nested data {i}-{j}</data>
                    </nested{j}>''')

            elements.append(f'''
            <item{i} xmlns:item="http://item.com" item:id="{i}">
                <header>Header {i}</header>
                <body>
                    {''.join(nested)}
                </body>
                <footer>Footer {i}</footer>
            </item{i}>''')

        return f'''<document xmlns="http://default.com"
                           xmlns:doc="http://document.com"
                           xmlns:meta="http://metadata.com">
            <meta:info>Large document test</meta:info>
            <doc:content>
                {''.join(elements)}
            </doc:content>
        </document>'''


def measure_performance(xml_input, test_name, iterations=10):
    """Измеряет производительность трансформации"""

    print(f"\n--- {test_name} ---")
    print(f"Размер XML: {len(xml_input):,} символов")
    print(f"Количество итераций: {iterations}")

    times = []

    # Прогрев
    canonicalize_xml(xml_input)

    # Измерения
    for i in range(iterations):
        start_time = time.time()
        result = canonicalize_xml(xml_input)
        end_time = time.time()

        execution_time = end_time - start_time
        times.append(execution_time)

        if i == 0:  # Сохраняем размер результата
            result_size = len(result)

    # Статистика
    avg_time = statistics.mean(times)
    min_time = min(times)
    max_time = max(times)
    median_time = statistics.median(times)

    print(f"Размер результата: {result_size:,} символов")
    print(f"Среднее время: {avg_time:.4f} сек")
    print(f"Минимальное время: {min_time:.4f} сек")
    print(f"Максимальное время: {max_time:.4f} сек")
    print(f"Медиана: {median_time:.4f} сек")
    print(f"Производительность: {len(xml_input) / avg_time:.0f} символов/сек")

    return avg_time, result_size


def compare_with_without_lxml():
    """Сравнение производительности с lxml и без"""

    print("\n=== Сравнение производительности с lxml и без ===")

    xml_input = generate_test_xml("medium")

    # Тест с lxml (если доступна)
    try:
        import lxml
        print("\nlxml доступна - тестируем с lxml")
        time_with_lxml = measure_performance(xml_input, "С lxml", 5)[0]
    except ImportError:
        print("\nlxml недоступна")
        time_with_lxml = None

    # Симуляция без lxml (сложно сделать напрямую)
    print("\nДля тестирования без lxml нужно временно удалить lxml")


def test_memory_usage():
    """Простой тест использования памяти"""

    print("\n=== Тест использования памяти ===")

    try:
        import psutil
        import os

        process = psutil.Process(os.getpid())

        # Измерение до
        memory_before = process.memory_info().rss

        # Генерируем и обрабатываем большой XML
        large_xml = generate_test_xml("large")
        result = transform_exc_c14n(large_xml)

        # Измерение после
        memory_after = process.memory_info().rss

        memory_used = memory_after - memory_before

        print(f"Память до: {memory_before / 1024 / 1024:.2f} MB")
        print(f"Память после: {memory_after / 1024 / 1024:.2f} MB")
        print(f"Использовано памяти: {memory_used / 1024 / 1024:.2f} MB")

    except ImportError:
        print("psutil недоступен для измерения памяти")
        print("Установите: pip install psutil")


def performance_comparison():
    """Сравнение производительности разных размеров XML"""

    print("\n=== Сравнение производительности ===")

    test_cases = [
        ("small", "Малый XML"),
        ("medium", "Средний XML"),
        ("large", "Большой XML")
    ]

    results = []

    for size, description in test_cases:
        xml_input = generate_test_xml(size)
        avg_time, result_size = measure_performance(xml_input, description, 5)
        results.append((description, len(xml_input), avg_time, result_size))

    # Сводная таблица
    print("\n=== Сводная таблица производительности ===")
    print(f"{'Тест':<15} {'Входной размер':<15} {'Время (сек)':<12} {'Выходной размер':<16} {'Скорость':<15}")
    print("-" * 80)

    for desc, input_size, time_taken, output_size in results:
        speed = input_size / time_taken
        print(f"{desc:<15} {input_size:<15,} {time_taken:<12.4f} {output_size:<16,} {speed:<15,.0f}")


def test_edge_cases():
    """Тест производительности на крайних случаях"""

    print("\n=== Тест крайних случаев ===")

    # Очень глубоко вложенный XML
    deep_xml = "<root>"
    for i in range(100):
        deep_xml += f"<level{i}>"
    deep_xml += "content"
    for i in range(99, -1, -1):
        deep_xml += f"</level{i}>"
    deep_xml += "</root>"

    measure_performance(deep_xml, "Глубоко вложенный XML", 3)

    # XML с множеством атрибутов
    attrs = " ".join([f'attr{i}="value{i}"' for i in range(50)])
    many_attrs_xml = f'<root {attrs}><content>Many attributes</content></root>'

    measure_performance(many_attrs_xml, "XML с множеством атрибутов", 3)

    # XML с множеством пространств имен
    namespaces = " ".join([f'xmlns:ns{i}="http://ns{i}.com"' for i in range(20)])
    many_ns_xml = f'<root {namespaces}><content>Many namespaces</content></root>'

    measure_performance(many_ns_xml, "XML с множеством пространств имен", 3)


if __name__ == "__main__":
    print("=== Тесты производительности ExcC14N ===")

    performance_comparison()
    compare_with_without_lxml()
    test_memory_usage()
    test_edge_cases()

    print("\n=== Тесты производительности завершены ===")
    print("\nРекомендации:")
    print("- Для лучшей производительности установите lxml")
    print("- Для больших документов рассмотрите потоковую обработку")
    print("- Кешируйте XmlCanonicalizer объекты при возможности")