from django.db import models


class Link(models.Model):
    find_url = models.URLField()
    domain = models.URLField(unique=True)
    create_date = models.DateField(null=True, blank=True)
    update_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=25, blank=True)
    is_dead = models.BooleanField()
    a = models.CharField(max_length=100, blank=True)
    ns = models.CharField(max_length=100, blank=True)
    cname = models.CharField(max_length=100, blank=True)
    mx = models.CharField(max_length=100, blank=True)
    txt = models.TextField(blank=True)
