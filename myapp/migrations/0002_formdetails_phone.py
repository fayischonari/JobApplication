# Generated by Django 3.2.12 on 2022-10-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdetails',
            name='phone',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
