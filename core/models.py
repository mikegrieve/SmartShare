from django.db import models
from django.contrib.auth.models import User, AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Topic(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=64)
    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=500, blank=True)
    img_src = models.URLField(blank=True)
    link = models.URLField(blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    up_votes = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=280, blank=True)
    score = models.PositiveSmallIntegerField(null=True, blank=True)
    def __str__(self):
        return '{} - {}'.format(self.user.username, self.item.name)