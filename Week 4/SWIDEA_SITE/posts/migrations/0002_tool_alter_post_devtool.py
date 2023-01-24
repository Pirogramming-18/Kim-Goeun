# Generated by Django 4.1.5 on 2023-01-18 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('tool_content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='devtool',
            field=models.ForeignKey(db_column='dev_tool', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Tool', to='posts.tool'),
        ),
    ]