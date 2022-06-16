import datetime
from os import listdir

PREFIX = "./git_projects/hillel_05_2022/lesson_5/homework"
LOG_FILE = PREFIX + "actions.log"


class MyLogger:
    def __init__(self, message: str):
        self.message = message

    def __call__(self, fn):
        def new_func(username, message):
            text = f"{datetime.now()} {username}: {message}"
            with open(LOG_FILE, "a") as f:
                f.write(f"{text}\n")
            return LOG_FILE

        return new_func


@MyLogger(message="sam")
def read_usb(username: str):
    files = listdir(PREFIX + "f-disc/")
    filtered = [file for file in files if not file.startswith(".")]
    return filtered


def log_action(text: str) -> None:
    with open(LOG_FILE, "a") as f:
        f.write(f"{text}\n")


# class Player:
#     name = ''
#     age = int()
#     number = int()
#     team = list[dict]

#     def __init__(self, name, age, number):
#         if not isinstance(name, str) and not isinstance(age, int) and \
#             not isinstance(number, int):
#                 raise Exception
#         self.name, self.age, self.number = name, age, number


#     def log(message: str) -> None:
#         def wrapper(func):
#             def inner(username):
#                 text = f"{datetime.now()} {username}: {message}"
#                 with open(LOG_FILE, "a") as f:
#                     f.write(f"{text}\n")

#                 return func(username)

#             return inner

#         return wrapper


#     def addPlayerByUniqueNumber(self, team, name: str, \
#  age: int, number: int,):
#         if self.number == team.number:
#             print(message="Didn't allowed")
#         else:
#             team.append(self)
#             print(message=f"New player added {self.name}")


# team: list[dict] = [
#     {Player.name: "John", Player.age: 20, Player.number: 1},
#     {Player.name: "Mark", Player.age: 33, Player.number: 3},
#     {Player.name: "Cavin", Player.age: 17, Player.number: 12},]

# team1: list[dict] = [
#                      {player1},
#                      {player2},
#                      {player3},
#                      ]

# player1 = Player("Bill", 20, 38)
# player2 = Player("Mike", 25, 43)
# player3 = Player("John", 20, 1)
# player4 = Player("Mark", 33, 3)
# player5 = Player("Kevin", 17, 12)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# playerFootballTeam.player1 = ('John', 20, 1)
# print(playerFootballTeam.player1)

# class logging(playerFootballTeam):

#     def log(message: str) -> None:
#         print(f"-> -> -> {message} <- <- <- ***")


# class remove_player(playerFootballTeam):

#         def rem_player(self. num):
#             if player["number"] == num:
#                 player_name = player["name"]
#             del players[index]
#             log(message=f"Deleting {player_name}")


# def main():
#     repr_players(team)

#     add_player(num=17, name="Cris", age=31)
#     add_player(num=17, name="Bob", age=39)
#     remove_player(players=team, num=17)

#     repr_players(team)


# class addingPlayer(footballTeam):

#     def add_player(num: int, name: str, age: int) -> None:
#         player = {"name": name, "number": num, "age": age}
#         logging(footballTeam).log(message=f"Adding {player['name']}")


# # player2 = player('Mark', 33, 3)
# # player2.log('player added')

# # player3 = player('Cavin', 17, 12)
# # print(player1.name
