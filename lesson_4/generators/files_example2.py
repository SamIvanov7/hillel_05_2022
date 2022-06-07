FILENAME = "./hillel_05_2022/lesson_4/generators/rockyou.txt"
SEARCH_KEYWORD = "admin"


def read_lines_find_admin() -> list:
    with open(FILENAME, encoding="utf-8") as file:
        return [word for word in file.readlines() if SEARCH_KEYWORD in word]


print("Lines 1: ", len(read_lines_find_admin()))
