# Generated by Django 3.0.7 on 2020-07-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolled',
            name='enrolled',
            field=models.CharField(max_length=64),
        ),
    ]
