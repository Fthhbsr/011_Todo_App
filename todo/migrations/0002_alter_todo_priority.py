# Generated by Django 4.1 on 2022-09-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('1', '😀'), ('2', '😁'), ('3', '😂'), ('4', '🤣'), ('5', '😃')], max_length=2),
        ),
    ]
