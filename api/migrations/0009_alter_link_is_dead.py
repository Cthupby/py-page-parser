# Generated by Django 4.0.3 on 2022-04-08 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_link_domain_alter_link_is_dead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='is_dead',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
