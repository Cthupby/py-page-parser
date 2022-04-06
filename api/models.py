from django.db import models


class Link(models.Model):
    find_url = models.URLField()
    domain = models.URLField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    country = models.CharField(max_length=100)
    is_dead = models.BooleanField()
    a = models.CharField(max_length=100)
    ns = models.URLField()
    cname = models.URLField()
    mx = models.URLField()
    txt = models.TextField()
