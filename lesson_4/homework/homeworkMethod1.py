from email.generator import Generator

FILENAME = "./lesson_4/generators/rockyou.txt"
SEARCH_KEYWORD = "user"


def readLinesFindUserGenerator() -> Generator:
    with open(FILENAME, encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if SEARCH_KEYWORD in line:
                yield line.replace("\n", "")
                continue


results = []
for line in readLinesFindUserGenerator():
    print("The new word found: ", (line))
    answer = input("Do you wanr to add this word to results? Y/N : ")
    if answer.lower() == "y":
        lineCorrected = line.replace("\n", "")
        results.append(lineCorrected)
        print(results, len(results))
        continue
    if answer.lower() == "n":
        continue
    if answer.lower() != "y" or answer.lower() != "n":
        print("Press only Y or N")
        break

print(results, len(results))
