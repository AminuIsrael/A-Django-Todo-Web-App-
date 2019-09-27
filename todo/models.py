from django.db import models

# Create your models here.
#create a class called todo item
class TodoItem(models.Model):
    content = models.TextField()