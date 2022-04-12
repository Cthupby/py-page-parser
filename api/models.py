from django.db import models


class Page(models.Model):
    page = models.URLField(unique=True)
    find_urls = models.ManyToManyField('Link', blank=True, related_name='pages')


class Link(models.Model):
    find_url = models.URLField(db_column='найденный url')
    domain = models.URLField(blank=True, db_column='domain')
    create_date = models.DateField(null=True, blank=True, db_column='create_date')
    update_date = models.DateField(null=True, blank=True, db_column='update_date')
    country = models.CharField(max_length=25, blank=True, db_column='country')
    is_dead = models.BooleanField(null=True, blank=True, db_column='isDead')
    a = models.CharField(max_length=100, blank=True, db_column='A')
    ns = models.CharField(max_length=100, blank=True, db_column='NS')
    cname = models.CharField(max_length=100, blank=True, db_column='CNAME')
    mx = models.CharField(max_length=100, blank=True, db_column='MX')
    txt = models.TextField(blank=True, db_column='TXT')
