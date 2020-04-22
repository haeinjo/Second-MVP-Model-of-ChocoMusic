import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as user_models
from core import models as core_models


class Command(BaseCommand):

    """
    class: Command
    author: haein
    des: User Command Model Definition
    date: 2020-04-22
    """

    help = "This command creates users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", type=int, default=1, help="How many users do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        positions = core_models.Position.objects.all()
        genres = core_models.Genre.objects.all()

        seeder.add_entity(
            user_models.User,
            number,
            {
                "email": lambda x: seeder.faker.ascii_email(),
                "alias": lambda x: seeder.faker.user_name(),
                "bio": lambda x: seeder.faker.paragraphs(),
                "gender": lambda x: random.choice(["male", "female", "other"]),
                "is_staff": False,
                "is_active": False,
                "is_superuser": False,
            },
        )

        created_users = seeder.execute()
        created_users = flatten(list(created_users.values()))

        for pk in created_users:
            user = user_models.User.objects.get(pk=pk)
            for position in positions:
                if random.randint(1, 4) > 2:
                    user.positions.add(position)

            for genre in genres:
                if random.randint(1, 4) > 2:
                    user.genres.add(genre)

            user.save()

        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
