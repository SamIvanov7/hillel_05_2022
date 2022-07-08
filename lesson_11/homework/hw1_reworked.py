from random import randint
from threading import Thread


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
print(f"thread status: {thread1.is_alive()}")
thread1.join()
print(f"thread status: {thread1.is_alive()}")

thread2.start()
thread3.start()

print(my_threads)
