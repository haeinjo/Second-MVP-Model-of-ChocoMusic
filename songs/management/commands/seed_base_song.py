from django.core.management.base import BaseCommand
from django_seed import Seed
from songs import models as song_models


class Command(BaseCommand):

    """
    class: Command
    author: haein
    des: BaseSong Command Model Definition
    date: 2020-04-22
    """

    help = "This command creates base_songs"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            default=1,
            help="How many base_songs do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        seeder.add_entity(
            song_models.BaseSong,
            number,
            {
                "composer": lambda x: seeder.faker.user_name(),
                "lyricist": lambda x: seeder.faker.user_name(),
                "singer": lambda x: seeder.faker.user_name(),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} base_songs created!"))
