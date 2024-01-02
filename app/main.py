import timeit

from single_thread import single_thread

number = 1

print(f"single_thread: {timeit.timeit(single_thread, number=number)}")
