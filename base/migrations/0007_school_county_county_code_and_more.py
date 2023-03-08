# Generated by Django 4.0.5 on 2022-07-24 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_subcounty_subcounty'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='county',
            name='county_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='extracounty',
            name='extra_county_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='national',
            name='National_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='subcounty',
            name='sub_county_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
