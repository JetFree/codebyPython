word = input("Веедите слово: ")
compare_predator = lambda string: "Это слово больше чем predator" \
    if string > "predator" else "Это слово меньше чем predator"
print(compare_predator(word))
