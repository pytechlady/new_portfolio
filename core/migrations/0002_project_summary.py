# Generated by Django 5.0.1 on 2024-02-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
