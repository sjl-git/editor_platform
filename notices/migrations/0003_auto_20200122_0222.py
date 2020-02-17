# Generated by Django 3.0.2 on 2020-01-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_noticevideo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='description',
        ),
        migrations.AddField(
            model_name='notice',
            name='deadline',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='notice',
            name='edited_length',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
    ]
