from random import randint
from threading import Thread

from hw1_calc_services import mid_average, summary

# When the application starts, three threads (T1, T2, T3) are launched

#     T1 thread fills the list with random numbers (10_000 elements)
#     T2 and T3 threads are waiting when the list is filled
#     When the list is full T2 and T3 are started
#     T2 thread finds the sum of the elements of the list
#     T2 thread finds the arithmetic avarage of the elements of the list
#     The resulting lists are displayed

list_rand_numbers = []


def gen_rand_numbers():
    for i in range(10_000):
        list_rand_numbers.append(randint(0, 100))


def main():
    thread1 = Thread(target=gen_rand_numbers, args=list_rand_numbers)
    thread2 = Thread(target=summary, args=(list_rand_numbers,))
    thread3 = Thread(target=mid_average, args=(list_rand_numbers,))

    thread1.start()
    thread1.join()
    thread2.start()
    thread3.start()
    thread2.join()
    thread3.join()


if __name__ == "__main__":
    main()
