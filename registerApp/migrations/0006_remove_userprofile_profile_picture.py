# Generated by Django 4.2.7 on 2023-12-19 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerApp', '0005_userprofile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
    ]
