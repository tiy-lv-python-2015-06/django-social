from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):

    username = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField(max_length=3)
    slam_jams = models.IntegerField()

    def __str__(self):
        return ("{}, {}, {}".format(self.username, self.email, self.slam_jams))


class Post(models.Model):

    title = models.CharField(max_length=50)
    image = models.ImageField()
    url_img = models.URLField()
    message = models.TextField()
    posted_by = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now_add=True)
    total_jams = models.ManyToManyField(Votes)

    def __str__(self):
        return self.objects


class Votes(models.Model):

    up_jams = models.ManyToManyField(Post)
    down_jams = models.ManyToManyField(Post)



