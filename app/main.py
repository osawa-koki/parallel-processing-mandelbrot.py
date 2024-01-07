import timeit

from multi_thread import multi_thread
from single_thread import single_thread

number = 1

print(f"single_thread: {timeit.timeit(single_thread, number=number)}")
print(f"multi_thread : {timeit.timeit(multi_thread, number=number)}")
