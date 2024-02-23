import random
import string
import os


def RandomStringGenerator(size=5, chars=string.ascii_lowercase + string.ascii_letters):
    return ''.join(random.choice(chars) for i in range(size))
