# Generated by Django 3.1.5 on 2021-01-30 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainers',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publicapp.courses'),
        ),
    ]
