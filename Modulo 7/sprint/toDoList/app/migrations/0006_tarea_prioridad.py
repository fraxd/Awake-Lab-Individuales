# Generated by Django 4.2.3 on 2023-07-10 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_prioridad_tarea_prioridad'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='prioridad',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='app.prioridad'),
            preserve_default=False,
        ),
    ]
