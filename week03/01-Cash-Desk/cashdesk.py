class Bill:

    def __init__(self, amount):
        self.amount = self.validate_amount(amount)
        self.total_count = 0

    def validate_amount(self, amount):
        if amount < 0:
            raise ValueError('Cannot use a negative number')

        elif not isinstance(amount, int):
            raise TypeError('Amount should be integer')

        else:
            return amount

    def __str__(self):
        return '"A {0}$ bill"'.format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.__str__())


a = Bill(10)
b = Bill(5)
c = Bill(10)

int(a)  # 10
str(a)  # "A 10$ bill"
print(a)  # A 10$ bill

a == b  # False
a == c  # True

money_holder = {}

money_holder[a] = 1  # We have one 10% bill

if c in money_holder:
    money_holder[c] += 1

    print(money_holder)  # { "A 10$ bill": 2 }

print('==================')


class BatchBill():

    def __init__(self, batch):
        self.batch = batch

    def __len__(self):
        return len(self.batch)

    def total(self):
        return sum([int(x) for x in self.batch])

    def __getitem__(self, index):
        return self.batch[index]


class CashDesk:

    def __init__(self):
        self.money = {}

    def take_money(self, money):
        if isinstance(money, Bill):
            if money not in self.money.keys():
                self.money[money] = 0

            self.money[money] += 1

        if isinstance(money, BatchBill):
            for bill in money:
                if bill not in self.money.keys():
                    self.money[bill] = 0

                self.money[bill] += 1

    def total(self):
        return sum([int(bill) * self.money[bill] for bill in self.money.keys()])

    def inspect(self):
        output = []

        output.append('We have a total of {0}$ in the desk'
                      .format(self.total()))
        output.append('We have the following count of bills, sorted in ascending order:')

        for bill in self.money.keys():
            output.append('{0}$ bills - {1}'
                          .format(int(bill), self.money[bill]))

        return '\n'.join(output)



























