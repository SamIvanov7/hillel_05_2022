FILENAME = "./lesson_4/generators/rockyou.txt"
SEARCH_KEYWORD = "user"


def readLinesFindUser() -> list:
    results = []
    with open(FILENAME, encoding="utf-8") as file:
        for word in file.readlines():
            if SEARCH_KEYWORD in word:
                print("The new word found: ", (word))
                answer = input("add this word to results? Y/N : ")
                if answer.lower() == "y":
                    wordCorrected = word.replace("\n", "")
                    results.append(wordCorrected)
                    print(results, len(results))
                    continue
                if answer.lower() == "n":
                    continue
                if answer.lower() != "y" or answer.lower() != "n":
                    print("Press only Y or N")
                    break

    return results, len(results)


print(readLinesFindUser())
