from random import choice
from string import ascii_letters

print(ascii_letters, "\n")


def generate_password(n: int) -> str:
    text = ""

    for i in range(n):
        text += choice(ascii_letters)

    return text


my_password = generate_password(10)


print(my_password)
