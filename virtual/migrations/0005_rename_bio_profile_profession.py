# Generated by Django 4.1.4 on 2023-01-23 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('virtual', '0004_rename_email_profile_bio_rename_name_profile_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='profession',
        ),
    ]
