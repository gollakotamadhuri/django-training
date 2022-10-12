import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ProTwo.settings')

import django

django.setup()

from faker import Faker

from AppTwo.models import User


def populate_user_data(n):
    Faker.seed(n)
    fake = Faker()

    for i in range(n):
        fake_firstname = fake.first_name()
        fake_lastname = fake.last_name()
        fake_email = fake.email()

        User.objects.get_or_create(first_name=fake_firstname,
                                   last_name=fake_lastname, email=fake_email)


if __name__ =='__main__':
    print("Populating fake data")
    populate_user_data(50)
    print("Fake data generated")
