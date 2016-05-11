from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length = 100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length = 255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        retunr self.headline

'''
saving objects
'''
from blog.models import Blog

b = Blog(name = 'something', tagline = 'about something')
b.save()

'''
saving Foreign and ManyToMany
'''
entry = Entry.objects.get(pk = 1)
some_blog = Blog.object.get(name = 'something')
entry.blog = some_blog
entry.save()

'''
ManyToManyField
'''
tanaka = Author.objects.create(name = 'tanaka')
entry.authors.add(tanaka)
