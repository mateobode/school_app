# Generated by Django 4.1.5 on 2023-01-29 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('grade', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('teacher_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=50)),
                ('student_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('feedback', models.CharField(blank=True, max_length=250)),
                ('semester', models.CharField(max_length=50)),
                ('assignments', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.assignment')),
                ('students', models.ManyToManyField(to='backend.student')),
                ('teachers', models.ManyToManyField(to='backend.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='students',
            field=models.ManyToManyField(to='backend.student'),
        ),
    ]