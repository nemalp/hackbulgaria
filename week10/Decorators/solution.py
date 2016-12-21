from decorators import *


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True


@log('log2.txt')
@encrypt(2)
def get_low():
    return "Get get get low"


@performance('log.txt')
def something_heavy():
    time.sleep(2)
    return "I am done!"


print(get_low())
print(deposit("RadoRado", 10))
print(say_hello("Hacker"))
print(something_heavy())
