import sqlite3
from colorama import Fore, Back, Style
import sys
sys.path.append('..')
from helpers.helpers import *
from user_interface.interface import CLI


class Menu:

    def __init__(self):
        self.interface = CLI()

    def start_interaction(self):
        delay_print('Welcome to our Cinema Reservation System!')
        delay_print('You can choose from the following commands:')
        show_available_commands()

        while True:
            command = input('>>> ')

            if command == 'show movies':
                self.interface.show_movies()

            elif command == 'make reservation':
                self.interface.make_reservation()

            elif command == 'exit':
                sys.exit()

            elif command == 'help':
                show_available_commands()

            else:
                if 'show movie projection' in command:
                    command = command.split()
                    if len(command) == 3:
                        print(Fore.RED +
                              'Missing arguments <id> [date]' +
                              Fore.RESET)

                    elif len(command) == 4:
                        movie_id = command[3]  # zero based indexing
                        self.interface.show_movie_projections(movie_id)

                    elif len(command) == 5:
                        movie_id = command[3]
                        date = command[4]
                        self.interface.show_movie_projections(movie_id, date)
                    else:
                        print(Fore.RED +
                              'At most two arguments expected <id> [date],' +
                              'received more' +
                              Fore.RESET)

                elif 'cancel reservation' in command:
                    self.interface.cancel_reservation()
                else:
                    print(Fore.RED + '\nUnrecognized command\n' + Fore.RESET)


def main():
    m = Menu()
    m.start_interaction()

if __name__ == '__main__':
    main()
