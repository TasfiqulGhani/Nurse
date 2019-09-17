# Generated by Django 2.2.5 on 2019-09-14 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20190914_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caretasks',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Task'),
        ),
        migrations.AlterField(
            model_name='medications',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
