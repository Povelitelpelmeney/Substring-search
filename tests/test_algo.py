import unittest
from algo import search_algorithms


def load_texts(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()


def load_answers(filename):
    return list(map(int, load_texts(filename).split()))


test1 = load_texts('tests/test_texts/test1.txt')
test1_answer = load_answers('tests/test_answers/test1_answer.txt')
test2 = load_texts('tests/test_texts/test2.txt')
test2_answer = load_answers('tests/test_answers/test2_answer.txt')
test3 = load_texts('tests/test_texts/test3.txt')
test3_answer = load_answers('tests/test_answers/test3_answer.txt')
test4 = load_texts('tests/test_texts/test4.txt')
test4_answer = load_answers('tests/test_answers/test4_answer.txt')
test5 = load_texts('tests/test_texts/test5.txt')
test5_substring = load_texts('tests/test_texts/test5_substring.txt')
test5_answer = load_answers('tests/test_answers/test5_answer.txt')
test6 = load_texts('tests/test_texts/test6.txt')
test6_substring = load_texts('tests/test_texts/test6_substring.txt')
test6_answer = load_answers('tests/test_answers/test6_answer.txt')
test7 = load_texts('tests/test_texts/test7.txt')
test7_substring = load_texts('tests/test_texts/test7_substring.txt')
test7_answer = load_answers('tests/test_answers/test7_answer.txt')

tests = dict()
tests['first'] = [test1, 'север ', test1_answer]
tests['second'] = [test2, 'DEF', test2_answer]
tests['third'] = [test3, '342765', test3_answer]
tests['fourth'] = [test4, '78', test4_answer]
tests['fifth'] = [test5, test5_substring, test5_answer]
tests['sixth'] = [test6, test6_substring, test6_answer]
tests['seventh'] = [test7, test7_substring, test7_answer]

class TestAlgorithms(unittest.TestCase):

    def test_search(self):
        for test in tests.keys():
            for algorithm in search_algorithms:
                actual = algorithm.findall(tests[test][1], tests[test][0])
                with self.subTest(f' {test} with {algorithm.name()}'):
                    self.assertEqual(actual, tests[test][2],
                                     f'actual: {actual}, '
                                     f'expected: {tests[test][2]}')


if __name__ == '__main__':
    unittest.main()
