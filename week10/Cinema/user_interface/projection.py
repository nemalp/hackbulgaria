from colorama import Fore


class Projection:

    def __init__(self, id):
        self.id = id
        self.hall = [['. ' for x in range(10)] for y in range(10)]
        # self.hall[3][3] = 'x '

    def show_hall(self):
        counter = 0
        print(Fore.CYAN +
              ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' +
              Fore.RESET)
        for row in self.hall:
            print(Fore.CYAN + str(counter) + Fore.RESET, ''.join(row))
            counter += 1

        print('\n')

    def reserve_seat(self, row, col):
        self.hall[row][col] = Fore.RED + 'x ' + Fore.RESET
        print('This is your reservation...')
