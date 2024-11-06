import time


start_time = time.perf_counter()
for i in range(100):
    import govnocode
end_time = time.perf_counter()

print(f"Тупой парсинг:\n\t{end_time - start_time}")

start_time = time.perf_counter()
for i in range(100):
    import lib
end_time = time.perf_counter()

print(f"Парсинг библиотекой:\n\t{end_time - start_time}")

start_time = time.perf_counter()
for i in range(100):
    import govnocode_with_regex
end_time = time.perf_counter()

print(f"Тупой парсинг + регулярные выражения:\n\t{end_time - start_time}")

start_time = time.perf_counter()
for i in range(100):
    import formal_grammar
end_time = time.perf_counter()

print(f"Парсинг с помощью формальных грамматик:\n\t{end_time - start_time}")