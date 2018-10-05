from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=64)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    up_votes = models.IntegerField(default=0)
    def __str__(self):
        return self.name