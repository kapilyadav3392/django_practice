# Generated by Django 3.2.7 on 2021-10-09 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0003_alter_data_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Birthdate',
            field=models.DateField(verbose_name='DD-MM-YYYY'),
        ),
    ]
