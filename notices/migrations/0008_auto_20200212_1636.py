# Generated by Django 3.0.2 on 2020-02-12 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0007_remove_notice_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-created']},
        ),
    ]