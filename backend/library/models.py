from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birthday_year}'


class Book(models.Model):
    title = models.CharField(max_length=64)
    authors = models.ManyToManyField(Author)


class Bio(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class TestBio(models.Model):
    title = models.CharField(max_length=64, primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


