# Generated by Django 3.2.5 on 2021-07-24 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoapp', '0003_auto_20210723_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='SummerNote',
        ),
    ]
