# Generated by Django 2.1.7 on 2019-05-25 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20190526_0156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='description',
        ),
    ]
