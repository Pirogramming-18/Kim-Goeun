# Generated by Django 4.1.5 on 2023-01-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_remove_post_author_remove_post_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='review',
            field=models.FloatField(null=True),
        ),
    ]
