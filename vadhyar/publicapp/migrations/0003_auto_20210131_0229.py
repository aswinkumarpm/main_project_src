# Generated by Django 3.1.5 on 2021-01-31 02:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0002_trainers_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fees',
            name='fees_id',
        ),
        migrations.RemoveField(
            model_name='interplacement',
            name='hod_id',
        ),
        migrations.RemoveField(
            model_name='interplacement',
            name='trainee_id',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='salary_id',
        ),
        migrations.AddField(
            model_name='fees',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fees',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='publicapp.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salary',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salary',
            name='trainer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publicapp.trainers'),
        ),
        migrations.AddField(
            model_name='salary',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='publicapp.customuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fees',
            name='student_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publicapp.students'),
        ),
        migrations.AlterField(
            model_name='fees',
            name='trainee_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publicapp.trainees'),
        ),
        migrations.AlterField(
            model_name='interplacement',
            name='course_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publicapp.courses'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='hod_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publicapp.hods'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='teacher_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publicapp.teacher'),
        ),
        migrations.CreateModel(
            name='StudyMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_type', models.CharField(choices=[('video', 'Video'), ('note', 'Note')], max_length=12)),
                ('file', models.FileField(upload_to='study-material')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publicapp.courses')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publicapp.subjects')),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]