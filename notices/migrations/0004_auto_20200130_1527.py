# Generated by Django 3.0.2 on 2020-01-30 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0003_auto_20200122_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticevideo',
            name='video',
            field=models.FileField(upload_to='notice_video'),
        ),
    ]
