import unittest
from benchmark import Benchmark


class TestBenchmark(unittest.TestCase):

    def test_benchmark(self):
        benchmark = Benchmark(1)
        self.skipTest('Benchmark is not testable')
