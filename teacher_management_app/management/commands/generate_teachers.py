from django.core.management.base import BaseCommand, CommandError
from teacher_management_app.models import Teacher
from faker import Faker
import random

fake = Faker()
subjects = ["Math", "English", "Ethics"]


class Command(BaseCommand):
    help = "Add teachers to data base"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, default=100)

    def handle(self, *args, **options):
        for i in range(options["number"]):
            t = Teacher.objects.create(
                first_name=fake.first_name(),
                surname=fake.last_name(),
                age=random.randint(21, 87),
                subject=random.choice(subjects),
            )

            self.stdout.write(
                self.style.SUCCESS(
                    '{}. Successfully added teacher "{}"'.format(i + 1, t.first_name)
                )
            )
