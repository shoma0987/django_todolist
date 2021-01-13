# Generated by Django 3.1 on 2021-01-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_todomodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todomodel',
            name='image',
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='duedate',
            field=models.DateField(blank=True, null=True),
        ),
    ]