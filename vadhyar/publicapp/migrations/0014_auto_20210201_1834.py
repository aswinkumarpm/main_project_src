# Generated by Django 3.1.5 on 2021-02-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0013_auto_20210201_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='subject_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
