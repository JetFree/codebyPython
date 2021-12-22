goal = 1000000

def calculate_years(start_income):
    years = 1
    while start_income < goal:
        start_income = start_income * 2
        years += 1
    return years


def calculate_start_income(years):
    final_sum = goal
    for _ in range(1, years):
        final_sum = final_sum / 2
    return final_sum


if __name__ == "__main__":
    income = 15625
    years = calculate_years(income)
    print("Понадобится %d лет чтобы стать миллионером при доходе %d$ за первый"
          " год" % (years, income))
    years = 10
    start_income = calculate_start_income(years)
    print("Понадобится заработать в первый год {:.2f}$ чтобы стать миллионером "
          "за {} лет".format(start_income, years))

