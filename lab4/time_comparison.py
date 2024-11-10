import time
import govnocode
import govnocode_with_regex
import lib
import xml_to_dict
import xml_to_json

testing_data = open('source/test1.xml', 'r', encoding='utf-8').read()
def time_test():
    start_time = time.perf_counter()
    for i in range(100):
        govnocode.parse_xml_to_json(testing_data)
    end_time = time.perf_counter()

    print(f"Тупой парсинг:\n\t{end_time - start_time}")

    start_time = time.perf_counter()
    for i in range(100):
        lib.parse_xml_to_json(testing_data)
    end_time = time.perf_counter()

    print(f"Парсинг библиотекой:\n\t{end_time - start_time}")

    start_time = time.perf_counter()
    for i in range(100):
        govnocode_with_regex.parse_xml_to_json(testing_data)
    end_time = time.perf_counter()

    print(f"Тупой парсинг + регулярные выражения:\n\t{end_time - start_time}")

    start_time = time.perf_counter()
    for i in range(100):
        xml_to_dict.parse_xml_to_json(testing_data)
    end_time = time.perf_counter()

    print(f"Парсинг с помощью формальных грамматик:\n\t{end_time - start_time}")

    start_time = time.perf_counter()
    for i in range(100):
        xml_to_json.parse_xml_to_json(testing_data)
    end_time = time.perf_counter()

    print(f"Парсинг авторским алгоритмом:\n\t{end_time - start_time}")

if __name__ == '__main__':
    time_test()