import string
import random
class GenerateRandom:
    def __init__(self, driver):
        self.driver = driver

    def generate_random_string(self):
        letters = string.ascii_letters
        random_string = ''.join(random.choice(letters) for _ in range(10))
        return random_string

    def generate_random_number(length):
        digits = string.digits
        random_number = ''.join(random.choice(digits) for _ in range(length))
        return random_number