# Generated by Django 3.2.6 on 2021-08-30 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_newpartener'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpartener',
            name='description',
            field=models.TextField(default=True),
        ),
        migrations.AlterField(
            model_name='newpartener',
            name='name',
            field=models.CharField(default=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='newpartener',
            name='name2',
            field=models.CharField(default=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='newpartener',
            name='name3',
            field=models.CharField(default=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='newpartener',
            name='name4',
            field=models.CharField(default=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='newpartener',
            name='name5',
            field=models.CharField(default=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='newpartener',
            name='name6',
            field=models.CharField(default=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='newpartener',
            name='name7',
            field=models.CharField(default=True, max_length=250),
        ),
    ]
