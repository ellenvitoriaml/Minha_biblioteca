# Generated by Django 4.2.4 on 2023-10-02 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_full_name_usuario_nome'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='biblioteca',
            table='bibliotecas',
        ),
        migrations.AlterModelTable(
            name='editora',
            table='editora',
        ),
        migrations.AlterModelTable(
            name='genero',
            table='genero',
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='usuario',
        ),
    ]