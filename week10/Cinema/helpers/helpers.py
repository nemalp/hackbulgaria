import sys
import time
from colorama import Fore


def delay_print(message):
    for char in message:
        sys.stdout.write(Fore.GREEN + char + Fore.RESET)
        sys.stdout.flush()
        time.sleep(0.07)

    sys.stdout.write('\n')


def show_available_commands():
    print(Fore.CYAN + '''
[1] - show movies
[2] - show movie projections <movie_id> [<date>]
[3] - make reservation
[4] - cancel reservation <name>
[5] - exit
[6] - help
''' + Fore.RESET)
