import random
import string


class BackendHelper:
    @staticmethod
    def create_random_aplhanumeric_string():
        token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(18))
        return token
