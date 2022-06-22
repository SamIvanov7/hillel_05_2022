from contextlib import contextmanager


def bar(func):
    def inner():
        return func()

    return inner


@bar
def foo():
    pass


# def my_open(filename: str):
# with open(filename) as file:
#     while True:
#         yield ...
#     lines = file.readlines()

# print(f"Lines number: {len(lines)}")

# return lines


@contextmanager
def my_open(filename):
    file = open(filename)
    lines = file.readlines()
    try:
        yield file
    finally:
        file.close()
        print(f"Lines: {len(lines)}")


FILENAME = "lesson_7_context_managers/rockyou.txt"

# data = my_open(FILENAME)
# with my_open(FILENAME) as file:
#     pass


class MyContextManager:
    def __enter__(self):
        ...

    def __exit__(self):
        ...


with MyContextManager() as data:
    pass


@contextmanager
def my_context_manager(*args, **kwargs):
    print("I am inside")
    try:
        yield "Hello message"
    finally:
        print("Exiting")


with my_context_manager() as result:
    print(result)
