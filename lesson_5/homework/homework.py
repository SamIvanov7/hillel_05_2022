from lib import answer

# - Complete the lesson example with team players

# - Add features:

#   - Now we can not add a players with the same number

#   - players_repr function gets next arguments:

#     - sorted: bool - if True print players sorted by number

#     - key: str - if sorted is True and key is specified prints team players
# sorted by key

#   - Add a new function `player_update` that update the player by `number`

#            Example:

#     def update_player(num: int) -> None:
#       ...

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# P.S.   players-repr == playerReprFunc


team: list[dict] = [
    {"name": "John", "age": 20, "number": 9},
    {"name": "Mark", "age": 33, "number": 67},
    {"name": "Bill", "age": 37, "number": 12},
    {"name": "Cavin", "age": 17, "number": 4},
    {"name": "Vova", "age": 19, "number": 43},
]


def log(message: str) -> None:
    print(f"-> -> -> {message} <- <- <-")


def playerAddingFunc(name: str, age: int, numb: int):
    playerNew: dict[str, int, int] = {"name": name, "age": age, "number": numb}

    if playerNew["number"] in [playerTmp["number"] for playerTmp in team]:
        log(message="This number is already taken. Choose another one")

    else:
        team.append(playerNew)
        log(message=f"You've just added {playerNew['name']}")
    return team


def playerRemFunc(playersList: list[dict], numb: int):
    for index, pl in enumerate(playersList):
        if pl["number"] == numb:
            pl_name = pl["name"]
            del playersList[index]
            log(message=f"You've just deleted {pl_name}")


def playerReprFunc(
                playersList: list[dict],
                sorter: bool = False,
                key: str = "number"
                ):
    if sorter:
        for pl in sorted(playersList, key=lambda x: x[key]):
            print(f"\t {pl['name']}, age :{pl['age']}, #  {pl['number']}")
    if not sorter:
        for pl in playersList:
            print(f"\t {pl['name']}, age :{pl['age']}, {pl['number']}")


def playerUpdateFunc(
    playersList: list[dict], numb: int, playerNUpd: str, playerAUpd: int
) -> None:
    if numb in [pl["number"] for pl in playersList]:
        for pl in playersList:
            if pl["number"] == numb:
                pl["name"] = playerNUpd
                pl["age"] = playerAUpd
                log(message=f"You've just updated player with number {numb}")
    else:
        log(message=f"Player with number {numb} does not exist")
    return


# def main():

#     playerReprFunc(team)

#     playerAddingFunc(numb=18, name="Vadik", age=30)
#     playerAddingFunc(numb=18, name="Artem", age=31)

#     playerRemFunc(playersList=team, numb=18)

#     playerUpdateFunc(team, numb=9, playerNameUpdated="Andrew",\n
#  playerAgeUpdated=35)
#     playerUpdateFunc(team, numb=1, playerNameUpdated="Ivan",\n
# playerAgeUpdated=40)

#     playerReprFunc(team, True)


print("Hi there... Here is your team:")
playerReprFunc(team)


def main():
    while True:
        input1 = input("Do you want to sort players by number Y/N:")
        if input1.lower() == "y":
            sorter = True
            playerReprFunc(team, sorter)

        input2 = input("Do you want to add player Y/N?:")
        if input2.lower() == "y":
            plName = str(input("Please enter player's Name:"))
            numb = int(input("Please enter player's Number:"))
            age = int(input("Please enter player's Age:"))
            playerAddingFunc(f"{plName}", f"{numb}", f"{age}")

        input3 = input(
            "You can delete this new added player. \
                Do you want to do this Y/N?:"
        )
        if input3.lower() == "y":
            num = int(input("Enter a number of player you want to delete:"))
            playerRemFunc(team, numb=f"{num}")

        input4 = input("Do you want to update player Y/N?:")
        if input4.lower() == "y":
            plName = str(input("Please enter player's Name:"))
            numb = int(input("Please enter player's Number:"))
            age = int(input("Please enter player's Age:"))
            playerUpdateFunc(team, f"{numb}", f"{plName}", f"{age}")

        if answer() is False:
            break


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
