# Generated by Django 3.2.5 on 2021-07-24 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoapp', '0004_auto_20210724_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
