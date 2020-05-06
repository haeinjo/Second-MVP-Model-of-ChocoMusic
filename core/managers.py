import random
from django.contrib.auth import models


class CustomManager(models.UserManager):

    """
    class: CustomManager
    author: haein
    des: Custom Manager Model Definition
    date: 2020-04-23
    """

    def random_records(self):
        all_self_number = self.count()
        self_number = random.randint(1, min(all_self_number, 5))
        begin_index = random.randint(0, all_self_number - self_number)
        end_index = begin_index + self_number
        added_selfs = self.all()[begin_index:end_index]

        return added_selfs
