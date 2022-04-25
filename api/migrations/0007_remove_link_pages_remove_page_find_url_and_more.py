# Generated by Django 4.0.3 on 2022-04-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_page_link_pages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='pages',
        ),
        migrations.RemoveField(
            model_name='page',
            name='find_url',
        ),
        migrations.AddField(
            model_name='page',
            name='find_urls',
            field=models.ManyToManyField(blank=True, related_name='pages', to='api.link'),
        ),
    ]
