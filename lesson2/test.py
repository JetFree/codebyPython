language = "Языки программирования: Pyp, Python, Goland, Jaba..."
language = language.replace("Pyp", "Php")
language = language.replace("Goland", "Golang")
language = language.replace("Jaba", "Java")
language = language[:23] + language[23:-2].upper()
print(language)
