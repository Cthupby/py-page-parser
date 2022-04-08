from django.db import models


class Page(models.Model):
    page = models.URLField(unique=True)
    find_urls = models.ManyToManyField('Link', blank=True, related_name='pages')


class Link(models.Model):
    find_url = models.URLField()
    domain = models.URLField(blank=True)
    create_date = models.DateField(null=True, blank=True)
    update_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=25, blank=True)
    is_dead = models.BooleanField(null=True, blank=True)
    a = models.CharField(max_length=100, blank=True)
    ns = models.CharField(max_length=100, blank=True)
    cname = models.CharField(max_length=100, blank=True)
    mx = models.CharField(max_length=100, blank=True)
    txt = models.TextField(blank=True)
