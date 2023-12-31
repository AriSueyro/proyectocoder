# Generated by Django 5.0 on 2024-01-04 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coderapp', '0004_curso_entregable_estudiante'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesor',
            options={'ordering': ['apellido'], 'verbose_name_plural': 'Profesores'},
        ),
        migrations.RenameField(
            model_name='entregable',
            old_name='entregado',
            new_name='hoy',
        ),
        migrations.RemoveField(
            model_name='entregable',
            name='fechaDeEntrega',
        ),
    ]
