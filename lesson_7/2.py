import sys

# john = "John"
# print(sys.getsizeof(john))
# john = 12
# print(sys.getsizeof(john))
# john = 12312412412
# print(sys.getsizeof(john))

person_d = {"name": "John", "phone": "380671442543"}
print(sys.getsizeof(person_d))

john = ("John", "380671442543")
print(sys.getsizeof(john))


# Binary search
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20


class Person:
    name = "John"
    phone = "380671442543"

    @classmethod
    def get_full_data(cls) -> str:
        return f"name: {cls.name}. phone {cls.phone}"


print(sys.getsizeof(Person))


print(person_d["name"])
print(Person.name)
print(Person.vars)  # raises AttributeError
