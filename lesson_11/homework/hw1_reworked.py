import random
from threading import Thread

numbers = []


def random_numbers():
    for i in range(10_000):
        numbers.append(random.randint(0, 10_000))


def summ(numbers) -> int:
    counter = 0
    for i in numbers:
        counter += i
    print(f"The summary is {counter}")


def mid_avarage(numbers):
    counter = 0
    for i in numbers:
        counter += i
    print(f"The mid_avarage is {counter / len(numbers)}")


def main():
    t1 = Thread(target=random_numbers)
    t1.start()
    t1.join()
    if t1.is_alive() is False:
        print(
            f"Thread1 has ended, list is completely filled and it length is: {len(numbers)}"
        )
        t2 = Thread(target=summ, args=(numbers,))
        t3 = Thread(target=mid_avarage, args=(numbers,))
        t2.start()
        t3.start()
        t2.join()
        t3.join()


if __name__ == "__main__":
    main()
