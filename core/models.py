from django.db import models


class TimeStamppedModel(models.Model):
    """
    class: TimeStamppedModel(abstract)
    author: haein
    des: Abstract Model for common time information
    date: 2020-03-12
    """

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class AbstractItem(models.Model):
    """
    class: AbstractItem
    author: haein
    des: 단순히 이름 정도 갖는 객체셋을 데이터베이스에서 관리하기 위한 가상 모델
    date: 2020-03-12
    """

    name = models.CharField(max_length=32)

    class Meta:
        abstract = True


class Genre(AbstractItem):
    """
    class: Genre
    author: haein
    des: 장르
    date: 2020-03-17
    """

    pass


class Position(AbstractItem):
    """
    class: Position
    author: haein
    des: 음악 역량
    date: 2020-03-17
    """

    pass
