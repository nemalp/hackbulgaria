import getpass
from time import ctime, strptime
from helpers.validator import validate_password
from controller import QueryController


class View:

    def __init__(self, controller):
        self.controller = controller

    def main_menu(self):
        print("Welcome to our bank service. You are not logged in. \n" +
              "Please register or login")

        while True:
            command = input(">>> ")

            if command == 'register':
                username = input("Enter your username: ")
                password = getpass.getpass("Enter your password: ")

                while not validate_password(username, password):
                    print('The password does not meet the required conditions')
                    password = getpass.getpass("Enter your password: ")

                email = input("Enter your email: ")

                self.controller.register(username, password, email)
                print("Registration Successfull")

            elif command == 'login':
                stop_login_loop = False
                invalid_login_attempts = 0
                username = input("Enter your username: ")
                banned_client = self.controller.is_banned(username)

                if banned_client:
                    ban_time = strptime(str(ctime(banned_client.ban_time)))
                    current_time = strptime(str(ctime()))

                    if ban_time > current_time:
                        print('{} is banned until {}'
                              .format(username, ctime(banned_client.ban_time)))
                    else:
                        self.controller.remove_ban(username)
                        print('{} was recently banned.'.format(username) +
                              ' Please use the login command again')
                else:
                    while stop_login_loop is False:
                        password = getpass.getpass("Enter your password: ")
                        logged_user = self.controller.login(username, password)

                        if logged_user:
                            self.logged_menu(logged_user)
                            stop_login_loop = True
                        else:
                            if invalid_login_attempts == 5:
                                self.controller.ban_client(username)
                                stop_login_loop = True
                                print('Too many login attempts. {} is banned for'
                                      .format(username) + ' 5 minutes')
                            else:
                                print("Login failed")
                                invalid_login_attempts += 1

            elif command.startswith('send-reset-password'):
                text = command.split(' ')
                if len(text) == 2:
                    username = text[1]
                    user = self.controller.select_client(username)

                    if user.email:
                        print('In order to use this option you' +
                              ' need to login with your gmail acc')
                        from_ = input('Email: ')
                        password = getpass.getpass('Password:')

                        self.controller.send_reset_password_email(from_,
                                                                  user.email,
                                                                  password)
                    else:
                        print('Uups! Something went wrong. It seems' +
                              'we cannot find your email in our system')

                else:
                    print('<username> is required for this command')

            elif command == 'help':
                print("login - for logging in!")
                print("register - for creating new account!")
                print("exit - for closing program!")

            elif command == 'exit':
                break
            else:
                print("Not a valid command")

    def logged_menu(self, logged_user):
        print("Welcome you are logged in as: " + logged_user.username)
        while True:
            command = input("Logged>>")

            if command == 'info':
                print("You are: " + logged_user.username)
                print("Your id is: " + str(logged_user.id))
                print("Your balance is:" + str(logged_user.balance) + '$')

            elif command == 'changepass':
                new_pass = getpass.getpass("Enter your new password: ")

                while not validate_password(logged_user.username,
                                            new_pass):
                    print('The password does not meet the required conditions')
                    new_pass = getpass.getpass("Enter your password: ")

                self.controller.change_pass(new_pass, logged_user)
                print('Congrats! You changed your password successfully.')

            elif command == 'change-message':
                new_message = input("Enter your new message: ")
                self.controller.change_message(new_message, logged_user)

            elif command == 'show-message':
                print('No message for you pal. Deal with it :)')
                # print(logged_user.message)

            elif command == 'help':
                print("info - for showing account info")
                print("changepass - for changing passowrd")
                print("change-message - for changing users message")
                print("show-message - for showing users message")


def main():
    v = View(QueryController())
    v.main_menu()

if __name__ == '__main__':
    main()
