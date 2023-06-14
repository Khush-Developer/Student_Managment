# Generated by Django 4.2 on 2023-06-14 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addcourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('fees', models.IntegerField()),
                ('duration', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=225)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Addstudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=200)),
                ('semail', models.EmailField(max_length=100)),
                ('smobile', models.IntegerField()),
                ('scollege', models.CharField(max_length=225)),
                ('sdegree', models.CharField(max_length=225)),
                ('scourses', models.ForeignKey(default='0', null=True, on_delete=django.db.models.deletion.CASCADE, to='student.addcourse')),
            ],
        ),
    ]
