# Generated by Django 5.0.1 on 2024-02-29 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_journal_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='rating',
        ),
    ]