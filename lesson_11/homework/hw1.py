from random import randint
from threading import Thread

# When the application starts, three threads (T1, T2, T3) are launched

#     T1 thread fills the list with random numbers (10_000 elements)
#     T2 and T3 threads are waiting when the list is filled
#     When the list is full T2 and T3 are started
#     T2 thread finds the sum of the elements of the list
#     T2 thread finds the arithmetic avarage of the elements of the list
#     The resulting lists are displayed


class GetPrimes3Threads:
    def __init__(self) -> None:
        self.numbers = []
        self.summ = 0
        self.average = 0

    def gen_rand_numbers(self):
        self.numbers = [randint(0, 100) for i in range(10_000)]

    def summary(self):
        self.summ = sum(self.numbers)

    def get_average(self):
        self.average = sum(self.numbers) / len(self.numbers)

    def __str__(self) -> str:
        return f"The summary is {self.summ}, The average is {self.average}"


my_threads = GetPrimes3Threads()

thread1 = Thread(target=my_threads.gen_rand_numbers())
thread2 = Thread(target=my_threads.summary())
thread3 = Thread(target=my_threads.get_average())

thread1.start()
thread1.join()

thread2.start()
thread3.start()

print(my_threads)
