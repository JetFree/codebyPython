targets = ["7 раз отмерь, 1 раз отрежь.", "Не имей 100 рублей, а имей 100"
                                          " друзей.", "1 за всех и все за 1."]
for str in targets:
    print(sum([int(digt) for digt in str[:-1].split() if digt.isdigit()]))
# print(sum([int(dig) for dig in list_str if str(dig).isdigit()]))
    # for word in str_arr:
    #     if word.isdigit():
    #         digits_list.append(int(word))
    # print(sum(digits_list))
