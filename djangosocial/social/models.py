from django.contrib.auth.models import User
from django.db import models

# Create your models here.
RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)


class Pinner(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField()
    board_count = models.IntegerField()
    pin_count = models.IntegerField()
    # Asymmetrical Relationships - the Twitter model
    relationships = models.ManyToManyField('self', through='Relationship',
                                           symmetrical=False,
                                           related_name='related_to')


    def __str__(self):
        return 'id: {} username: {} first_name: {} last_name: {}'.\
            format(self.id, self.username, self.first_name, self.last_name)


class Relationship(models.Model):
    from_person = models.ForeignKey(Pinner, related_name='from_people')
    to_person = models.ForeignKey(Pinner, related_name='to_people')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)


class Board(models.Model):
    creator = models.ForeignKey(Pinner)
    name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.CharField(max_length=200)
    image = models.ImageField()
    created = models.DateTimeField()

    def __str__(self):
        return 'id: {} name: {} url: {} description: {} creator: {}'.\
            format(self.id, self.name, self.url,
                   self.description, self.creator)


class Pin(models.Model):
    creator = models.ForeignKey(Pinner)
    board = models.ManyToManyField(Board)
    link = models.URLField()
    image = models.ImageField()
    created = models.DateTimeField()

    def __str__(self):
        return 'id: {} link: {} board: {} creator: {}'.\
            format(self.id, self.link, self.board, self.creator)
