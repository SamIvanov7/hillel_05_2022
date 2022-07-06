def summary(lst: list):
    counter = 0
    for i in lst:
        counter += i
    print(f"The summ of elements in list: {counter}")


def mid_average(lst):
    counter = 0
    for i in lst:
        counter += i
    average = counter / len(lst)
    print(f"the middle-average of the elements in list: {average}")
