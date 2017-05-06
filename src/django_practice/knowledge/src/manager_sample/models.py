from django.db import models

# Create your models here.


class DocumentQueryset(models.QuerySet):
    def pdfs(self):
        return self.filter(file_type='pdf')

    def smaller_than(self, size):
        return self.filter(size__lt=size)

class DocumentManager(models.Manager):

    def get_queryset(self):
        return DocumentQueryset(self.model, using=self._db)

    def pdfs(self):
        return self.queryset.pdfs()


    def smaller_than(self, size):
        return self.queryset.smaller_than(size__lt=size)


class Document(models.Model):
    name = models.CharField(max_length=30)
    size = models.PositiveIntegerField(default=0)
    file_type = models.CharField(max_length=10, blank=True)

    objects = DocumentManager()
