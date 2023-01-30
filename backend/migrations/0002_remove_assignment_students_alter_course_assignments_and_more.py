# Generated by Django 4.1.5 on 2023-01-29 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='students',
        ),
        migrations.AlterField(
            model_name='course',
            name='assignments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.assignment'),
        ),
        migrations.AlterField(
            model_name='course',
            name='feedback',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='students',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.student'),
            preserve_default=False,
        ),
    ]
