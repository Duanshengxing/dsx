from django.db import models

# Create your models here.
from author.models import Author
from publisher.models import Publisher


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    publishers = models.ManyToManyField(Publisher)
    publish_date = models.DateField()

    def __str__(self):
        return self.title