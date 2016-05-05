from django.db import models
from django.forms import ModelForm


class Author(models.Model):
    name = models.CharField(max_length = 120)
    title = models.CharField(max_length = 120)
    birth_date = models.DateField(blank = True, null = True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length = 100)
    authors = models.ManyToManyField(Author)


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']
