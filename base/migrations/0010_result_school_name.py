# Generated by Django 4.0.5 on 2022-09-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='school_Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]