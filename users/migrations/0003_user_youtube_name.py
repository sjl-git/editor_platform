# Generated by Django 3.0.2 on 2020-01-24 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='youtube_name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
