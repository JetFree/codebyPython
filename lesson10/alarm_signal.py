import signal
import sys

import vlc
from colorama import Fore


def handler(x, y): # Никаких аргументов сюда передавать не нужно
    explosion()
    sys.exit()


def play_sound():
    p = vlc.MediaPlayer("alarm.mp3")
    p.audio_set_volume(50)
    p.play()


def request_password():
    try:
        password = input(Fore.RESET + "Введите код отмены операции самоуничтожения: ")
    except (KeyboardInterrupt, EOFError, UnboundLocalError):
        print("Выполнение программы было остановлено внешним фактором")
        return False
    else:
        return password


def explosion():
    print(Fore.LIGHTMAGENTA_EX + "\nБА-БАХ!!!")


def verify_password():
    for _ in range(3):
        if request_password() == "swordfish":
            print(Fore.GREEN + "Операция самоуничтожения отменена!")
            return True
        else:
            print(Fore.RED + "Код не принят!")


if __name__ == "__main__":
    play_sound()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(30)
    print(Fore.RED + "ВНИМАНИЕ! Запущен механизм самоуничтожения!")
    if not verify_password():
        explosion()
    signal.alarm(0)
    sys.exit()
