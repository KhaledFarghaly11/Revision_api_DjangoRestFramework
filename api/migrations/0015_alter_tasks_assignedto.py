# Generated by Django 3.2.6 on 2021-08-31 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210831_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='assignedTo',
            field=models.ManyToManyField(blank=True, to='api.Employee'),
        ),
    ]