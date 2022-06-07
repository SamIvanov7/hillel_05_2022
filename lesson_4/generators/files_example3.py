from email.generator import Generator

FILENAME = "./hillel_05_2022/lesson_4/generators/rockyou.txt"
SEARCH_KEYWORD = "admin"


def read_lines_find_admin_generator() -> Generator:
    with open(FILENAME, encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if SEARCH_KEYWORD in line:
                print(line)
                yield line.replace("\n", "")
                continue


# for line in read_lines_find_admin_generator():
#     print(line)

print("Lines 2: ", read_lines_find_admin_generator())
