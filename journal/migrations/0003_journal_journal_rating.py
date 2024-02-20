# Generated by Django 5.0.1 on 2024-02-08 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_rename_user_journal_journal_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='journal_rating',
            field=models.CharField(choices=[('positive', 'positive'), ('negative', 'negative')], default=5, max_length=15),
            preserve_default=False,
        ),
    ]