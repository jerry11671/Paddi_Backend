# Generated by Django 5.0.1 on 2024-01-29 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessment',
            name='expression_analysis',
        ),
        migrations.AddField(
            model_name='healthgoal',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
