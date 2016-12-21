import time
import logging
from datetime import datetime
from functools import wraps


def accepts(*args):
    types = enumerate(args)

    def accepter(func):
        def decorator(*args, **kwargs):
            for idx, type_ in types:
                if not isinstance(args[idx], type_):
                    raise TypeError('Argument {} of {} is not {}'
                                    .format(idx+1,
                                            func.__name__,
                                            type_.__name__))
            return func(*args, **kwargs)
        return decorator
    return accepter


def encrypt(key):
    def encryptor(func):
        def decorator(*args, **kwargs):
            L2I = dict(zip("abcdefghijklmnopqrstuvwxyz", range(26)))
            I2L = dict(zip(range(26), "abcdefghijklmnopqrstuvwxyz"))
            plaintext = func()
            ciphertext = ""

            for ch in plaintext:
                if ch.isalpha():
                    if ch.isupper():
                        ciphertext += I2L[(L2I[ch.lower()] + key) % 26].upper()

                    else:
                        ciphertext += I2L[(L2I[ch] + key) % 26]
                else:
                    ciphertext += ch
                    return ciphertext
        return decorator
    return encryptor


def performance(file_name):
    def timer(func):
        logging.basicConfig(filename=file_name, level=logging.INFO)

        def decorator(*args, **kwargs):
            start_time = time.time()
            result = func()
            runtime = time.time() - start_time

            logging.info('{} was called and took {:.2f} seconds to complete'
                         .format(func.__name__, runtime))
            return result
        return decorator
    return timer


def log(file_name):
    def logger(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            with open(file_name, 'a') as f:
                f.write('{} was called at {}\n'
                        .format(func.__name__, datetime.now()))
            return func(*args, **kwargs)
        return decorator
    return logger
