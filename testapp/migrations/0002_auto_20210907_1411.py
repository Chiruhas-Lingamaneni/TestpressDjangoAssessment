# Generated by Django 2.2.12 on 2021-09-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='score_to_pass',
            field=models.IntegerField(),
        ),
    ]
