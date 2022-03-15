import requests


def format_str(currency):
    return "{:9s}{:.2f} руб.".format(currency + ":", float(json_content[f'{currency}']))


if __name__ == "__main__":
    resp = requests.get("https://belarusbank.by/api/kursExchange?city=Минск")
    cur_list = ["USD_in",
                "USD_out",
                "EUR_in",
                "EUR_out",
                "RUB_in"
                ]
    json_content = resp.json()[0]
    print("Курсы валют в Минске сегодня:\n")
    for currency in cur_list:
        print(format_str(currency))
