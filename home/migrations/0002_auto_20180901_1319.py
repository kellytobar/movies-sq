# Generated by Django 2.0.6 on 2018-09-01 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='sinopsis',
            field=models.CharField(max_length=500),
        ),
    ]
