# Generated by Django 5.0.1 on 2024-02-29 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='price',
            new_name='total_price',
        ),
        migrations.AddField(
            model_name='record',
            name='inital_price',
            field=models.IntegerField(null=True),
        ),
    ]
