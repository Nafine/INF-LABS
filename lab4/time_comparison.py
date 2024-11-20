import time
from src import govnocode_with_regex, lib, xml_to_dict, govnocode, xml_to_json

testing_data = open('input/test1.xml', 'r', encoding='utf-8').read()
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

    print(f"Первая не особо удачная попытка написть формалки:\n\t{end_time - start_time}")

if __name__ == '__main__':
    time_test()