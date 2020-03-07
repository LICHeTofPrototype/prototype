# Generated by Django 3.0.4 on 2020-03-07 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(null=True, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='birth_date'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='which_sex',
            field=models.CharField(max_length=1, null=True, verbose_name='sex'),
        ),
    ]
