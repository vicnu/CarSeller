# Generated by Django 3.2.6 on 2021-08-28 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carseller_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carbodytype',
            options={},
        ),
        migrations.AlterModelOptions(
            name='carmodel',
            options={},
        ),
        migrations.AlterModelOptions(
            name='carstate',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={},
        ),
        migrations.AlterModelOptions(
            name='carvender',
            options={},
        ),
        migrations.AlterModelOptions(
            name='drivetype',
            options={},
        ),
        migrations.AlterModelOptions(
            name='fueltype',
            options={},
        ),
        migrations.AlterModelOptions(
            name='gearbox',
            options={},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={},
        ),
        migrations.AlterModelOptions(
            name='sellrequest',
            options={'ordering': ('-CreationDate',)},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
    ]
