# Generated by Django 4.2.5 on 2024-05-17 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Json', '0005_push_to_pm_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='push_to_pm_file',
            name='status',
        ),
        migrations.AddField(
            model_name='my_upload_file',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]