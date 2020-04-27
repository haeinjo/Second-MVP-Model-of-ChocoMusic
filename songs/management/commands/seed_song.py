import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from songs import models as song_models
from users import models as user_models
from core import models as core_models


class Command(BaseCommand):

    """
    class: Command
    author: haein
    des: Song Command Model Definition
    date: 2020-04-23
    """

    help = "This command creates songs"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", type=int, default=1, help="How many songs do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        base_songs = song_models.BaseSong.objects.all()
        users = user_models.User.objects.all()
        positions = core_models.Position.objects.all()

        seeder.add_entity(song_models.Song, number, {
            "base_song": random.choice(base_songs),
            # Project가 필요해서 만들고 오겠다.
            })

        created_roles = seeder.execute()
        created_roles = flatten(list(created_roles.values()))

        for role in created_roles:
            role = song_models.Role.objects.get(pk=role)
            temp_user1 = random.choice(users)
            role.users.add(temp_user1)
            if random.randint(1, 4) > 2:
                temp_user2 = random.choice(users)
                if temp_user1 != temp_user2:
                    role.users.add(temp_user2)
            role.save()

        self.stdout.write(self.style.SUCCESS(f"{number} roles created!"))
