# Generated by Django 4.0.3 on 2022-04-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_link_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='create_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='update_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
