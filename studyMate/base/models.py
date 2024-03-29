from django.db import models
from django.contrib.auth.models import User #built-in db table Django Framework

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # database table relationship
    topic=  models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants',blank=True)  # many to many relationship.
    updated = models.DateTimeField(auto_now=True) #updates each time an item is updated
    created = models.DateTimeField(auto_now_add=True) #runs ONLY once when an item is created in DB

    class Meta:
        ordering = ['-updated', '-created'] # '-' enables order by descending order(new first)

    def __str__(self):
        return self.name
    
    def desc(self):
        return self.description[0:120]  # get first 50 characters of the description attribute

    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # database table relationship
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-updated', '-created'] # '-' enables order by descending order(new first)

    def __str__(self):
        return self.body[0:50] # get first 50 characters at Recent activity section(body attribute)