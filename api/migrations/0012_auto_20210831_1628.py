# Generated by Django 3.2.6 on 2021-08-31 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210830_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partener',
            name='details',
            field=models.ManyToManyField(to='api.Details'),
        ),
        migrations.AlterField(
            model_name='partener',
            name='tasks',
            field=models.ManyToManyField(to='api.Tasks'),
        ),
    ]
