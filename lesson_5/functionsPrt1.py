# from pprint import pprint as print

LOGGING = True

team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def log(message: str) -> None:
    print(f"-> -> -> {message} <- <- <- ***")


def add_player_by_unique_number(num: int, name: str, age: int) -> None:
    lst1 = []
    for i in team:
        lst1.append(i[list(i.keys())[2]])
        player = {"name": name, "number": num, "age": age}
    if num not in lst1():
        team.append(player)
    else:
        print("Same number found")
    log(message=f"Adding {player['name']}")


add_player_by_unique_number(20, "loh", 34)
add_player_by_unique_number(20, "pidr", 36)
print(team)
# def repr_players(players: list[dict]) -> None:
#     print("TEAM:")
#     for player in players:
#         print(f"\t{player['number']} " f"Name: {player['name']}, \
#  Age: {player['age']}")
#     print("\n")


# d


# # def remove_player(players: list[dict], num: int) -> None:
# #     for index, player in enumerate(players):
# #         if player["number"] == num:
# #             player_name = player["name"]
# #             del players[index]
# #             log(message=f"Deleting {player_name}")


# # def main():
# #     repr_players(team)

# #     add_player(num=17, name="Cris", age=31)
# #     add_player(num=17, name="Bob", age=39)
# #     remove_player(players=team, num=17)

# #     repr_players(team)


# # if __name__ == "__main__":
# #     main()
# # else:
# #     raise SystemExit("This module in only for running")
