from django.db import models

# Create your models here.

class Forums(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    forum_body = models.TextField()

def __str__(self):
    return self.title
