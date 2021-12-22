history = 'История Python, одного из самых простых языков программирования, началась в 1989 году.'

first_option = history[32:37] + history[3:5]
print(first_option)

index = history.find("про")
second_option = history[index:index + 5] + history[3:5]
print(second_option)

third_option = history[32:36] + history[2:5]
print(third_option)

forth_option = history[4:1:-1] + history[35:31:-1]
print(forth_option[::-1])
