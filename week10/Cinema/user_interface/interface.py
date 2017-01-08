import sqlite3
from colorama import Fore, Back, Style
import sys
sys.path.append('..')
from settings.general_settings import *
from queries.manage_db_queries import *
from database.manage_database import *
from helpers.helpers import *
from projection import Projection


class CLI:

    def __init__(self):
        self.DB = sqlite3.connect('../database/' + DB_NAME)
        self.DB.row_factory = sqlite3.Row
        self.c = self.DB.cursor()
        self.parser = argparse.ArgumentParser()

    def show_movies(self):
        movies = self.c.execute(MOVIES_ORDERED_BY_RATING)

        print(Fore.GREEN + '\nMovies ordered by rating:\n' + Fore.RESET)
        for movie in movies:
            print('[{}] - {} ({})'.format(movie['id'],
                                          movie['name'],
                                          Fore.YELLOW + str(movie['rating']) +
                                          Fore.RESET))
        print('\n')

    def show_movie_projections(self, id, date=None):
        self.c.execute(SELECT_MOVIE_BY_ID, [id])
        movie = self.c.fetchone()

        if id and date:
            projections = self.c.execute(ALL_PROJECTIONS_FOR_MOVIE_BY_DATE,
                                         [id, date])
            print("\nProjections for movie '{}' on date {}:\n"
                  .format(Fore.YELLOW + movie['name'] + Fore.RESET,
                          Fore.CYAN + date + Fore.RESET))

            for p in projections:
                print('[{}] - {} ({})'.format(p['id'], p['time'], Fore.GREEN +
                                              p['type'] + Fore.RESET))
            print('\n')

        else:
            projections = self.c.execute(ALL_PROJECTIONS_FOR_MOVIE, [id])
            print("\nProjections for movie '{}':\n"
                  .format(Fore.YELLOW + movie['name'] + Fore.RESET))
            for p in projections:
                print('[{}] - {} ({})'.format(p['id'],
                                              p['date'], Fore.GREEN +
                                              p['type'] + Fore.RESET))
            print('\n')

    def make_reservation(self):
        print(Fore.LIGHTMAGENTA_EX +
              'You need to a user in the system to make reservations!' +
              Fore.RESET)
        username = input('Username: ')
        password = input('Password: ')
        login_ = login(username, password)

        if login_:
            number_of_tickets = input('Choose number of tickets:> ')
            self.show_movies()

            movie_id = input(Fore.GREEN + 'Choose a movie by id:> ' +
                             Fore.RESET)
            '''
            TODO
            If the available spots for a projection are less than the number of
            tickets needed, print an appropriate message and stay at step 6;
            '''
            self.show_movie_projections(movie_id)
            projection = input(Fore.GREEN + 'Choose a projection by id:> ' +
                               Fore.RESET)
            # The code below is just for testing purposes and should be removed
            p = Projection(projection)
            p.reserve_seat(3, 3)
            print('Available seats (marked with a dot):')
            p.show_hall()

    def cancel_reservation(self):
        print('Cannot cancel reservation at this time. Please try again later.')


if __name__ == '__main__':
    main()
