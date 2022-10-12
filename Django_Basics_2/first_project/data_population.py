import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import random

import django

django.setup()
from faker import Faker

from first_app.models import AccessRecord, Topic, Webpage


def populate_topic():
    topics_list = ["Social Media", "Music", "News", "Games", "Well-being","Finance","Movies","Books"]
    count = len(topics_list)

    topic= Topic.objects.get_or_create(topic_name=topics_list[random.choice(range(count))])[0]
    
    return topic

def populate_data(n=5):
    
    fake = Faker()
    Faker.seed(24)
    
    for i in range(n):
        # For webpage
        topic = populate_topic()
        fake_company = fake.company()
        fake_url = fake.url()

        webpage = Webpage.objects.get_or_create(topic=topic,name=fake_company,url=fake_url)[0]
        

        # For accessrecord

        fake_date = fake.date()
        accrec = AccessRecord.objects.get_or_create(name=webpage,date=fake_date)
        


if __name__ == '__main__':
    print("Ready to populate records")
    populate_data(50)
    print("Populated!")
