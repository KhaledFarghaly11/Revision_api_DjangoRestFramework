# Generated by Django 3.2.6 on 2021-09-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_rename_details_tasks_details_tasks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='fullName',
        ),
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
