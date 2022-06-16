PREFIX = "/home/sam//git_projects/hillel_05_2022/lesson_5/homework/"
LOG_FILE = PREFIX + "actions.log"


team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def log1(message: str) -> None:
    print(f"-> -> -> {message} <- <- <- ***")


def log(message: str):
    def wrapper(func):
        def inner(playername):
            text = f"-> -> -> {message} <- <- <- ***"
            with open(LOG_FILE, "a") as f:
                f.write(f"{text}\n")

            return func(playername)

        return inner

    return wrapper


@log(message="logging repr")
def repr_players(
    players: list[dict], sort_players: bool = False, key: str = "number"
) -> None:
    print("\nTEAM:")
    if sort_players:
        for player in sorted(players, key=lambda x: x[key]):
            print(
                f"\t{player['number']} \
                Name: {player['name']}, Age: {player['age']}"
            )
    else:
        for player in players:
            print(
                f"\t{player['number']} \
                Name: {player['name']}, Age: {player['age']}"
            )
    print("\n")


@log(message="logging add")
def add_player(num: int, name: str, age: int) -> None:
    new_player = {"name": name, "number": num, "age": age}
    if new_player["number"] in [player["number"] for player in team]:
        log1(message="Number is being used by other players")
    else:
        team.append(new_player)
        log1(message=f"Adding {new_player['name']}")


def remove_player(players: list[dict], num: int) -> None:
    for index, player in enumerate(players):
        if player["number"] == num:
            player_name = player["name"]
            del players[index]
            log(message=f"Deleting {player_name}")


def update_player(players: list[dict], num: int, new_name: str, new_age: int):
    if num in [player["number"] for player in team]:
        for player in players:
            if player["number"] == num:
                player["name"], player["age"] = new_name, new_age
                log(message=f"Updating player number {num}")
    else:
        log(message=f"No player with number {num}")


def main():

    repr_players(team)

    add_player(num=17, name="Chris", age=31)
    add_player(num=17, name="Bob", age=39)

    remove_player(players=team, num=17)

    update_player(team, 1, "Rick", 21)
    update_player(team, 77, "Tony", 27)

    repr_players(team, True)
    repr_players(team, True, "age")


if __name__ == "__main__":
    main()
