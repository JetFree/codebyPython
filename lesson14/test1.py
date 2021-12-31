class ForeignFilm:

    def __init__(self, title, name, surname):
        self.title = title
        self.name = name
        self.surname = surname

    def print_info(self):
        print(f"{self.title} - в главной роли {self.name} {self.surname}")


class RussianFilm(ForeignFilm):
    pass


film_list = [ForeignFilm("Хищник", "Арнольд", "Шварцнеггер"),
             ForeignFilm("Железный человек", "Роберт", "Дауни мл."),
             ForeignFilm("Джон Уик", "Киану", "Ривз"),
             ForeignFilm("Матрица", "Киану", "Ривз"),
             ForeignFilm("Кто Я", "Том", "Шиллинг"),
             RussianFilm("Легенда 17", "Данила", "Козловский"),
             RussianFilm("Духлесс", "Данила", "Козловский"),
             RussianFilm("Брат 2", "Сергей", "Бодров"),
             RussianFilm("Жмурки", "Никита", "Михалков"),
             RussianFilm("Бригада", "Сергей", "Безруков")]

for film in film_list:
    film.print_info()
