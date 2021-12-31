def date_track(func):

    from datetime import datetime

    def print_date(*args):
        result = func(*args)
        print(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        return result

    return print_date

@date_track
class Test:

    def __init__(self):
        print("hello")

    @date_track
    def count(self):
        print("=" * 10)


Test().count()
