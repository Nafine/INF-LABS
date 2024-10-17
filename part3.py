import re
import unittest
import sys
#Пусть для тестов:
#Буквы: А И Р
#Расстояние: 2

#Решает в общем виде
#Можно передать три любые буквы и расстояние между ними
def matches(input_str, letters, distance):
    pattern = r'\b[^letters\s]*LETTER1[^letters\s]{distance}LETTER2[^letters\s]{distance}LETTER3[^letters\s]*\b'
    pattern = pattern.replace('letters', letters)
    pattern = pattern.replace('distance', str(distance))

    if (distance < 0 or len(letters) != 3 or len(set(letters)) != len(letters)):
        print('Wrong arguments')
        sys.exit(1)
    for i in range(1,4):
        pattern = pattern.replace(f'LETTER{i}', letters[i-1])
    return re.findall(pattern, input_str)


print(matches('123ИпппМопоП 223ыпыИаааМопоП233', 'ИМП', 3))
print(matches('2343hfhFjj00GjhgfH24 армянеFлюблGюармHян', 'FGH', 4))
print(matches('123KLO324 KLO', 'KLO', 0))
class TestLab(unittest.TestCase):
    assert_map = {'АирИооР АрАИппР АааИааР'
                  : ['АирИооР', 'АааИааР'],
                  'АААИИИР АклИрпР ПомОечКа МаВроДи АрмЯнЕ АббИкоР 123АммИооР123 квадроА__И__Рбобер'
                  : ['АклИрпР', 'АббИкоР', '123АммИооР123', 'квадроА__И__Рбобер'],
                  'А  И  Р АмоНгуС АбрИкоР АндРеЙ'
                  : ['АбрИкоР'],
                  'АфрОдиТа БалАкшИн АпоИлоРАбоБусЫ ПоставьтеДопБаллы КекУтуС ЯЛюблюАяяИееРСвоюМаму'
                  : ['ЯЛюблюАяяИееРСвоюМаму'],
                  'Бутылку разбивают и говорят: «АобИоаР». Что будешь делать? АмоИмоР - сказал мне тот бомАсуИждР'
                  : ['АобИоаР', 'АмоИмоР', 'бомАсуИждР']
                  }

    def test(self):
        i = 1
        for test in self.assert_map:
            self.assertEqual(matches(test, 'АИР', 2), self.assert_map[test])
            print(f'test_{i} completed')
            i += 1
