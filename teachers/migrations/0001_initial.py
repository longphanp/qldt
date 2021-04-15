# Generated by Django 3.2 on 2021-04-15 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_account', to=settings.AUTH_USER_MODEL)),
                ('archivements', models.ManyToManyField(db_table='teacher_archivement', related_name='teachers', to='persons.Achievement')),
                ('teacher_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='persons.personinfo')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]
