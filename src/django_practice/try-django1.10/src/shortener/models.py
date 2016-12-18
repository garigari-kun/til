from django.db import models

from .utils import create_shortcode, code_generator



class KirrURLManager(models.Manager):

    def all(self, *args, **kwargs):
        qs_super = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_super.filter(active=True)
        return qs

    def refresh_shortcode(self):
        qs = KirrURL.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        return 'New codes made: {}'.format(new_codes)




class KirrURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, default='abc', unique=True, blank=True)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = KirrURLManager()

    def __str__(self):
        return self.url

    # overriding save
    def save(self, *args, **kwargs):
        if self.shortcode == None or self.shortcode != '':
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)
