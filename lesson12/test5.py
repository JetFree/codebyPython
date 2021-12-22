import random
from colorama import Fore


def do_throw():
    return random.randint(1, 6) + random.randint(1, 6)


def print_winner(name, score):
    print(Fore.GREEN + f"Игрок {name} набрал {score} очк. You winner")


def print_score(name, score):
    print(Fore.RESET + f"Игрок {name} набрал {score} очк.")


def get_results():
    return {"Дима": do_throw(), "Вова": do_throw()}


def print_results(results):
    results = {k: results[k] for k in sorted(results, key=results.get, reverse=True)}
    items = list(results.items())
    print_winner(items[0][0], items[0][1])
    print_score(items[1][0], items[1][1])


def game_engine():
    while (result_dict := get_results()).get("Дима") == result_dict.get("Вова"):
        print_score("Дима", result_dict.get("Дима"))
        print_score("Вова", result_dict.get("Вова"))
        print("Очки у обоих игроков совпали, перебрасываем кости")
    print_results(result_dict)


if __name__ == "__main__":
    game_engine()


