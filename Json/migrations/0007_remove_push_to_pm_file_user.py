# Generated by Django 4.2.5 on 2024-05-17 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Json', '0006_remove_push_to_pm_file_status_my_upload_file_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='push_to_pm_file',
            name='user',
        ),
    ]
