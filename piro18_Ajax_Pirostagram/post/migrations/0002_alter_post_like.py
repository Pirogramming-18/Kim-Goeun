# Generated by Django 4.1.5 on 2023-01-24 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
