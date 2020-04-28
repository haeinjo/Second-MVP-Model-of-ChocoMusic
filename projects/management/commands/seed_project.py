import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from projects import models as project_models
from teams import models as team_models


class Command(BaseCommand):

    """
    class: Command
    author: haein
    des: Project Command Model Definition
    date: 2020-04-23
    """

    help = "This command creates projects"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            default=1,
            help="How many projects do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        teams = team_models.Team.objects.all()

        seeder.add_entity(
            project_models.Project,
            number,
            {
                "description": lambda x: seeder.faker.paragraphs(),
                "team": lambda x: random.choice(teams),
            },
        )

        created_projects = seeder.execute()
        created_projects = flatten(list(created_projects.values()))

        for project in created_projects:
            project = project_models.Project.objects.get(pk=project)
            participants = project.team.users.random_records()
            for participant in participants:
                project.participants.add(participant)
            project.save()

        self.stdout.write(self.style.SUCCESS(f"{number} projects created!"))
