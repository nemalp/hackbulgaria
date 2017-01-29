import string


def validate_password(username, password):
    if len(password) <= 8 or has_capital_letter(password) is False or \
            is_username_in_password(username, password) is True or \
            has_special_character(password) is False or \
            has_numeric(password) is False:
        return False

    return True


def has_capital_letter(password):
    return bool([l for l in password if l.isupper()])


def has_numeric(password):
    return bool([l for l in password if l.isnumeric()])


def has_special_character(password):
    return len(set(string.punctuation).intersection(password)) > 0


def is_username_in_password(username, password):
    return username in password
