from tests.test_algo import tests
from algo import search_algorithms
import matplotlib.pyplot as plt
import time
import tracemalloc


class Benchmark:

    def __init__(self, n_times):
        self.tests = tests
        self.n_times = n_times
        self.test_time = {}
        self.test_mem = {}
        for test in self.tests.keys():
            self.test_time[test] = \
                {alg.name(): [] for alg in search_algorithms}
            self.test_mem[test] = \
                {alg.name(): [] for alg in search_algorithms}

    def report(self, name: str, samples, scale: str):
        data = self.test_time
        figure, axes = plt.subplots(len(data), figsize=(30, 90))
        for i, test in enumerate(data):
            for alg in data[test]:
                x_arr = range(len(samples[test][alg]))
                y_arr = list(map(lambda x: x, samples[test][alg]))
                axes[i].plot(x_arr, y_arr, label=alg)
                axes[i].set_title(test)
                axes[i].set_xlabel('runs')
                axes[i].set_ylabel(scale)
                axes[i].legend()
        figure.savefig(name, format='png')

    def run(self):
        for test in self.tests.keys():
            print('__________TEST: ' + test + '__________')
            for alg in search_algorithms:
                print(alg.name())
                for i in range(self.n_times):
                    tracemalloc.start()
                    first_time = time.time()
                    alg.findall(tests[test][1], tests[test][0])
                    timer = int((time.time() - first_time) * 1000)
                    mem = tracemalloc.get_traced_memory()[1]
                    tracemalloc.stop()
                    self.test_time[test][alg.name()].append(timer)
                    self.test_mem[test][alg.name()].append(mem)


if __name__ == '__main__':
    n = int(input())
    benchmark = Benchmark(n)
    start_time = int(round(time.time()))
    benchmark.run()
    finish_time = int(round(time.time()))
    print(f'Benchmark ends in {finish_time - start_time} seconds')
    benchmark.report('results_time.png', benchmark.test_time, 'time')
    benchmark.report('results_mem.png', benchmark.test_mem, 'memory')
