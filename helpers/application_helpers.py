import datetime
import random
import string
import os


class BackendHelper:
    @staticmethod
    def create_random_aplhanumeric_string():
        token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(18))
        return token


def get_working_directory():
    working_directory = os.getcwd()
    return working_directory


def get_now():
    now = datetime.datetime.now()
    return now
