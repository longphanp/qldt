# Generated by Django 3.2.2 on 2021-06-15 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import school.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=8)),
                ('location', models.CharField(max_length=16)),
                ('homeroom_teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_class', to='teachers.teacher')),
            ],
            options={
                'db_table': 'classroom',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=32)),
                ('group_course', models.CharField(choices=[('Sc', 'Science'), ('So', 'Society'), ('Ph', 'Physical')], max_length=2)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('N', 'Normal'), ('B', 'Broken'), ('O', 'Old')], default='N', max_length=1)),
                ('device_name', models.CharField(max_length=128)),
                ('amount', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'device',
            },
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('day_of_week', models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thusday'), ('Fri', 'Friday'), ('Sat', 'Satuday'), ('Sun', 'Sunday')], max_length=3)),
                ('shifts', models.SmallIntegerField()),
                ('semester', models.SmallIntegerField(default=1)),
                ('school_year', models.SmallIntegerField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetables', to='school.classroom')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetables', to='school.course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetables', to='teachers.teacher')),
            ],
            options={
                'db_table': 'timetable',
            },
        ),
        migrations.CreateModel(
            name='TeachingInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('school_year', models.CharField(max_length=250)),
                ('semester', models.SmallIntegerField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.classroom')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
            options={
                'db_table': 'teaching_information',
            },
        ),
        migrations.CreateModel(
            name='StudyDocument',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('file', models.FileField(upload_to=school.models.teacher_directory_path)),
                ('study_week', models.SmallIntegerField()),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.classroom')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='school.course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='teachers.teacher')),
            ],
            options={
                'db_table': 'study_document',
            },
        ),
        migrations.CreateModel(
            name='DeviceManage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('day_of_week', models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thusday'), ('Fri', 'Friday'), ('Sat', 'Satuday'), ('Sun', 'Sunday')], max_length=3)),
                ('shifts', models.SmallIntegerField()),
                ('week', models.SmallIntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to=settings.AUTH_USER_MODEL)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_manages', to='school.device')),
            ],
            options={
                'db_table': 'device_manage',
            },
        ),
        migrations.CreateModel(
            name='ClassRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('classification', models.CharField(choices=[('A', 'Excellent'), ('B', 'Good'), ('C', 'Quite good'), ('D', 'Not good'), ('F', 'Fail')], default='A', max_length=1)),
                ('study_week', models.SmallIntegerField()),
                ('attendant', models.SmallIntegerField()),
                ('note', models.TextField(null=True)),
                ('day_of_week', models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thusday'), ('Fri', 'Friday'), ('Sat', 'Satuday'), ('Sun', 'Sunday')], max_length=3)),
                ('shifts', models.SmallIntegerField()),
                ('semester', models.SmallIntegerField(default=1)),
                ('school_year', models.SmallIntegerField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrecords', to='school.classroom')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrecords', to='school.course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrecords', to='teachers.teacher')),
            ],
            options={
                'db_table': 'class_record',
            },
        ),
    ]
