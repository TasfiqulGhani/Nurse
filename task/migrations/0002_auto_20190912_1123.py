# Generated by Django 2.2.5 on 2019-09-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='caretask',
        ),
        migrations.AddField(
            model_name='task',
            name='caretask',
            field=models.ManyToManyField(to='task.CareTasks'),
        ),
        migrations.RemoveField(
            model_name='task',
            name='medications',
        ),
        migrations.AddField(
            model_name='task',
            name='medications',
            field=models.ManyToManyField(to='task.Medications'),
        ),
    ]
