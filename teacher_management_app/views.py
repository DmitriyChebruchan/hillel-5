from django.shortcuts import render
import random
from faker import Faker

fake = Faker()
subjects = ["Math", "English", "Ethics"]


def teacher_generator():
    first_name = fake.first_name()
    surname = fake.surname()
    age = random(21, 87)
    subject = random.choice(subjects)
