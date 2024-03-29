from django.db import models


class Page(models.Model):
    '''
    Page model for parsing to find urls
    '''
    page = models.URLField(unique=True)
    find_urls = models.ManyToManyField('Link', blank=True, related_name='pages')


class Link(models.Model):
    '''
    Model for the link that the parser will find on the page
    '''
    find_url = models.URLField(db_column='найденный url', unique=True)
    domain = models.URLField(blank=True, null=True, db_column='domain')
    create_date = models.DateField(blank=True, null=True, db_column='create_date')
    update_date = models.DateField(blank=True, null=True, db_column='update_date')
    country = models.CharField(blank=True, max_length=25, db_column='country')
    is_dead = models.BooleanField(blank=True, null=True, db_column='isDead')
    a = models.TextField(blank=True, db_column='A')
    ns = models.TextField(blank=True, db_column='NS')
    cname = models.TextField(blank=True, db_column='CNAME')
    mx = models.TextField(blank=True, db_column='MX')
    txt = models.TextField(blank=True, db_column='TXT')
