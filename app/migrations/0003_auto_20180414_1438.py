# Generated by Django 2.0.2 on 2018-04-14 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_friend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='topics',
            new_name='subscriptions',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='nSubscribers',
        ),
    ]