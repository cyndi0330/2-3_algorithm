
import time
from random import randrange
from sorting_algorithm import bubble, insertion, selection, merge, quick

import matplotlib.pyplot as plt


def measure_running_time(func, A):
    s_time = time.time()
    func(A)
    return time.time() - s_time


if __name__ == '__main__':
    bubble_times = []
    insertion_times = []
    selection_times = []
    merge_times = []
    quick_times = []
    built_in_times = []

    for i in range(3, 19):
        print(f'step{i - 2}')
        size = 2 ** i

        test_data = [randrange(-(2 ** 32 - 2), 2 ** 32 - 2) for _ in range(size)]

        if i < 14:
            bubble_times.append(measure_running_time(bubble, test_data[:]))
            insertion_times.append(measure_running_time(insertion, test_data[:]))
            selection_times.append(measure_running_time(selection, test_data[:]))
        merge_times.append(measure_running_time(merge, test_data[:]))
        quick_times.append(measure_running_time(quick, test_data[:]))


        s_time = time.time()
        sorted(test_data)
        built_in_times.append(time.time() - s_time)

    plt.figure(figsize=(8, 6))
    plt.grid(True)
    plt.xticks([i for i in range(16)], [f'2^{i}' for i in range(3, 19)])

    plt.plot(bubble_times, label='bubble', color='c', marker='*')
    plt.plot(insertion_times, label='insertion', color='g', marker='X')
    plt.plot(selection_times, label='selection', color='b', marker='D')
    plt.plot(merge_times, label='merge', color='black', marker='^')
    plt.plot(quick_times, label='quick', color='y', marker='<')
    plt.plot(built_in_times, label='built-in', color='r', marker='o')

    plt.legend(loc='upper left')

    plt.savefig(fname='running_time_sorting.png', format='png')
    plt.show()
