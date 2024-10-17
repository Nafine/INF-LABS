import re
import unittest

def count_smiles(input_str):
    return len(re.findall(';<{=', input_str))

class TestLab(unittest.TestCase):
    assert_map = { 'Я похож на ;<{= но мне 13 и я как маленький ;<{= и я очень быстрый и накаченный как ;<{= и я тоже качаюсь и у меня как у ;<{= волосы мышцы пресс как у ;<{= и руки как у ;<{= и я как ;<{= не устаю'
                   : 7,
                   ';<{=;<{=;<{=;<{=;<{= monkey flip'
                   : 5,
                   'Е;<{=й рот этого казино, ;<{=, ты кто такой, ;<{=, чтоб это сделать?!'
                   : 3,
                   '  ;<{\n=   '
                   : 0,
                   ';<{) :<{= ;>{= ;<(='
                   : 0
                  }
    def test(self):
        i = 1
        for test in self.assert_map:
            self.assertEqual(count_smiles(test), self.assert_map[test])
            print(f'test_{i} completed')
            i += 1