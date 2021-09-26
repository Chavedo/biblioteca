from faker import Faker
from faker.providers import BaseProvider
import random

fake = Faker()


class EmailProvider(BaseProvider):
    def email(self):
        return f'{fake.last_name().lower()}@gmail.com'


class UsernameProvider(BaseProvider):
    def username(self):
        return random.randint(1111, 9999)
