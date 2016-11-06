class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        self._balance = get_quantity(balance)
        self.currency = currency
        self._history = ['Account was created']

    def __str__(self):
        return "Bank account for {0} with balance of {1}{2}".format(
            self.name, self.balance(), self.currency)

    def __int__(self):
        self._history.append('__int__ check -> {}{}'.format(
            self.balance(), self.currency))

        return self.balance()

    def deposit(self, amount):
        self._history.append('Deposited {}{}'.format(amount, self.currency))
        self._balance += get_quantity(amount)

    def balance(self):
        self._history.append('Balance check -> {}{}'.format(
            self._balance, self.currency))

        return self._balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            self._history.append('{}{} was withdrawed'.format(
                amount, self.currency))

            return True

        else:
            self._history.append('Withdraw for {}{} failed.'.format(
                amount, self.currency))

            return False

    def transfer_to(self, account, amount):
        if account.currency != self.currency:
            return False

        if amount > self._balance:
            return False

        self._balance -= amount
        account._balance += amount

        self._history.append('Transfer to {0} for {1}{2}'.format(
            account.name, amount, self.currency))

        account._history.append('Transfer from {0} for {1}{2}'.format(
            self.name, amount, account.currency))

        return True

    def history(self):
        return self._history


def get_quantity(n):
    if n < 0:
        raise ValueError

    return n


def main():
    account = BankAccount("Rado", 0, "$")
    account.deposit(1000)

    rado = BankAccount("Rado", 1000, "BGN")
    ivo = BankAccount("Ivo", 0, "BGN")
    rado.transfer_to(ivo, 500)
    rado.balance()
    ivo.balance()

    print(rado.history())
    print(ivo.history())

if __name__ == '__main__':
    main()
