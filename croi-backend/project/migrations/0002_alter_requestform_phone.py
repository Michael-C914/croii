# Generated by Django 4.0.1 on 2022-01-24 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestform',
            name='phone',
            field=models.IntegerField(),
        ),
    ]