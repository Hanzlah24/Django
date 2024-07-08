from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
