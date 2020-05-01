import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from playlists import models as playlist_models
from users import models as user_models
from songs import models as song_models


class Command(BaseCommand):

    """
    class: Command
    author: haein
    des: PlayList Command Model Definition
    date: 2020-04-30
    """

    help = "This command creates playlists"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            default=1,
            help="How many playlists do you want to created",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        seeder.add_entity(
            playlist_models.PlayList,
            number,
            {
                "description": lambda x: seeder.faker.paragraphs(),
                "category": lambda x: random.choice(
                    playlist_models.ListCategory.objects.all()
                ),
                "user": lambda x: random.choice(user_models.User.objects.all()),
            },
        )

        created_lists = seeder.execute()
        created_lists = flatten(list(created_lists.values()))

        for l in created_lists:
            created_list = playlist_models.PlayList.objects.get(pk=l)
            song_cnt = song_models.Song.objects.count()
            random_number = random.randint(min(2, song_cnt), min(50, song_cnt))

            songs = song_models.Song.objects.all().order_by("?")[2:random_number]

            for song in songs:
                created_list.songs.add(song)

            created_list.save()

        self.stdout.write(self.style.SUCCESS(f"{number} playlists are created!"))
