# Generated by Django 2.0.7 on 2018-08-06 07:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fil_auth', '0007_auto_20180806_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='idf',
            field=models.CharField(default=uuid.UUID('852170a5-d3e4-464f-ba45-4e78a018ce73'), max_length=64, verbose_name='Identification key'),
        ),
    ]
