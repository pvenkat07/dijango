# Generated by Django 3.0.6 on 2020-05-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='pin_no',
        ),
        migrations.AddField(
            model_name='member',
            name='year',
            field=models.DateField(null=True),
        ),
    ]
