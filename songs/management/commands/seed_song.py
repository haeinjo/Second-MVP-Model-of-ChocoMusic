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
        projects = project_models.Project.objects.all()
        genres = core_models.Genre.objects.all()

        seeder.add_entity(
            song_models.Song,
            number,
            {
                "base_song": lambda x: song_models.BaseSong.objects.first(),
                "composer": lambda x: user_models.User.objects.first(),
                "lyricist": lambda x: user_models.User.objects.first(),
                "project": lambda x: random.choice(projects),
                "genre": lambda x: random.choice(genres),
                "is_covered": lambda x: random.choice([True, False]),
            },
        )

        created_songs = seeder.execute()
        created_songs = flatten(list(created_songs.values()))

        for song in created_songs:
            song = song_models.Song.objects.get(pk=song)
            participants = user_models.User.objects.filter(projects=song.project)
            participants_cnt = participants.count()
            song.composer = random.choice(participants)
            song.lyricist = random.choice(participants)
            base_song = song_models.BaseSong.objects.create(
                title=seeder.faker.word(),
                composer=song.composer.email,
                lyricist=song.lyricist.email,
            )
            positions_cnt = core_models.Position.objects.exclude(name="보컬").count()
            positions = core_models.Position.objects.order_by("?").exclude(name="보컬")[
                : random.randint(1, positions_cnt)
            ]
            for position in positions:
                role = song_models.Role.objects.create(position=position, song=song)

                participants_ = participants.order_by("?").all()[
                    : random.randint(1, participants_cnt)
                ]
                for participant in participants_:
                    role.users.add(participant)
                role.save()

            role = song_models.Role.objects.create(
                position=core_models.Position.objects.get(name="보컬"), song=song
            )
            participants_ = participants.order_by("?").all()[
                : random.randint(1, min(2, participants_cnt))
            ]
            participant_list = []
            for participant in participants_:
                participant_list.append(participant.email)
                role.users.add(participant)
            role.save()
            base_song.singer = ", ".join(participant_list)
            base_song.save()
            song.base_song = base_song
            song.save()

        self.stdout.write(self.style.SUCCESS(f"{number} songs and roles created!"))
