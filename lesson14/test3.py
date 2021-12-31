class EllipsoidUtil:

    @staticmethod
    def calculate():
        try:
            a = float(input("Введите первую полуось: "))
            b = float(input("Введите вторую полуось: "))
        except ValueError:
            print("Введите корректные данные!")
        except KeyboardInterrupt:
            print("Выполнение программы прервано")
        else:
            s = 3.14 * float(a) * float(b)
            print(f"{s:.2f}")


class ConeUtil:

    @staticmethod
    def calculate():
        try:
            h = float(input("Введите высоту конуса: "))
            r = float(input("Введите радиус конуса: "))
        except ValueError:
            print("Введите корректные данные!")
        except KeyboardInterrupt:
            print("Выполнение программы прервано")
        else:
            v = (float(h)/3) * 3.14 * float(r) ** 2
            print(f"{v:.2f}")


ConeUtil.calculate()
EllipsoidUtil.calculate()
