import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from songs import models as song_models
from core import models as core_models
from projects import models as project_models
from users import models as user_models


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
        projects = project_models.Project.objects.all()

        seeder.add_entity(
            song_models.Song,
            number,
            {
                "base_song": lambda x: random.choice(base_songs),
                "project": lambda x: random.choice(projects),
            },
        )

        created_songs = seeder.execute()
        created_songs = flatten(list(created_songs.values()))

        positions = core_models.Position.objects.random_records()
        for song in created_songs:
            song = song_models.Song.objects.get(pk=song)
            for position in positions:
                role = song_models.Role.objects.create(position=position, song=song,)
                user_number = user_models.User.objects.count()
                random_number = random.randint(1, min(3, user_number))
                users = user_models.User.objects.filter(projects=song.project).order_by(
                    "?"
                )[:random_number]
                
                for user in users:
                    role.users.add(user)

                role.save()

        self.stdout.write(self.style.SUCCESS(f"{number} songs and roles created!"))
