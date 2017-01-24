'''
Models for the Tweet app
'''
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tweet(models.Model):
    '''
    Model class for a Tweet
    '''
    content = models.CharField(max_length=140)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)