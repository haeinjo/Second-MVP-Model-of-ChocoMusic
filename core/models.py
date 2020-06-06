from django.db import models


class TimeStamppedModel(models.Model):

    """
    class: TimeStamppedModel(abstract)
    author: haein
    des: Abstract Model for common time information
    date: 2020-03-12
    """

    created = models.DateField(auto_now_add=True, null=True)
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

    def __str__(self):
        return f"{self.name}"


class Position(AbstractItem):

    """
    class: Position
    author: haein
    des: 음악 역량
    date: 2020-03-17
    """

    def __str__(self):
        return f"{self.name}"


class Tag(AbstractItem):

    """
    class: Tag
    author: haein
    des: 태그
    date: 2020-05-28
    """

    def __str__(self):
        return self.name


class Borough(AbstractItem):

    """
    class: Borough
    author: haein
    des: 자치 구
    date: 2020-06-05
    """

    city = models.ForeignKey("City", related_name="boroughs", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city} - {self.name}"


class City(AbstractItem):

    """
    class: City
    author: haein
    des: 자치 시
    date: 2020-06-05
    """

    def __str__(self):
        return self.name
