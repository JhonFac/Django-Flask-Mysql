# Generated by Django 3.2.9 on 2022-06-04 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20220603_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuerpo_técnico',
            name='FNacimiento',
            field=models.CharField(default=b'I00\n', max_length=100),
        ),
        migrations.AlterField(
            model_name='jugadores',
            name='Fnacimiento',
            field=models.CharField(default=b'I00\n', max_length=100),
        ),
    ]
