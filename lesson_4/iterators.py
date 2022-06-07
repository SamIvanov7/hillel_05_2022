for i in range(10):
    print(i)

range(10)
type(range(10))
type(type(range(10)))

source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
type(source)

names = ["dima", "dasha", "vasya", "petya", "kolya"]

print("out source names:")
# for l in names:
#     print(l)
# print("\n\n")

# breakpoint()


data = iter(names)
print("out iter names:")
# data.__next__()
# data.__next__()
# data.__next__()
# data.__next__()
# data.__next__()

while True:
    try:
        print(data.__next__())
    except StopIteration:
        break
