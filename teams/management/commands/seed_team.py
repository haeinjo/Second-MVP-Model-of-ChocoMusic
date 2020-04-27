import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from teams import models as team_models
from users import models as user_models


class Command(BaseCommand):

    """
    class: Command
    author: haein
    des: Team Command Model Definition
    date: 2020-04-23
    """

    help = "This command creates teams"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", type=int, default=1, help="How many teams do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        seeder.add_entity(
            team_models.Team,
            number,
            {
                "name": lambda x: seeder.faker.user_name(),
                "active_region": lambda x: seeder.faker.address(),
                "is_solo": lambda x: random.randint(1, 2) == 1,
            },
        )

        created_teams = seeder.execute()
        created_teams = flatten(list(created_teams.values()))

        for team in created_teams:
            team = team_models.Team.objects.get(pk=team)
            added_users = user_models.User.objects.random_records()

            users_positions = []
            users_genres = []

            for user in added_users:
                users_positions += user.positions.all()
                users_genres += user.genres.all()
            users_positions = set(users_positions)
            users_genres = set(users_genres)

            # Give users, positions and genres to Team
            for user in added_users:
                team.users.add(user)

            for position in users_positions:
                team.positions.add(position)

            for genre in users_genres:
                team.genres.add(genre)

            team.save()

        self.stdout.write(self.style.SUCCESS(f"{number} teams created!"))
