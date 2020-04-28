import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from recruitments import models as recruitment_models
from core import models as core_models
from teams import models as team_models


class Command(BaseCommand):

    """
    class: Command
    author: haein
    des: Recruitment Command Model Definition
    date: 2020-04-27
    """

    help = "This command creates recruits"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            default=1,
            help="How many recruits do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        seeder.add_entity(
            recruitment_models.Recruit,
            number,
            {
                "description": lambda x: seeder.faker.address(),
                "team": random.choice(team_models.Team.objects.all()),
            },
        )

        created_recruits = seeder.execute()
        created_recruits = flatten(list(created_recruits.values()))

        for recruitment in created_recruits:
            recruitment = recruitment_models.Recruit.objects.get(pk=recruitment)
            genres = core_models.Genre.objects.random_records()
            for genre in genres:
                recruitment.genres.add(genre)
            recruitment.save()
            # make RecruitedPosition
            positions = core_models.Position.objects.random_records()
            for position in positions:
                recruitment_position = recruitment_models.RecruitedPosition(
                    number=random.randint(1, 3), position=position, recruit=recruitment,
                )

                recruitment_position.save()

        self.stdout.write(self.style.SUCCESS(f"{number} recruits created!"))
