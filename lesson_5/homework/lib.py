def answer():
    question = input("Do you want to repeat this operation? Y/N: ")
    if question.lower() == "y":
        return True
    elif question.lower() == "n":
        return False
    else:
        print("Unknown command...")
        exit()
