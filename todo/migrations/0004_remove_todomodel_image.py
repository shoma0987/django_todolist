# Generated by Django 3.1 on 2020-11-29 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todomodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todomodel',
            name='image',
        ),
    ]
