# Generated by Django 4.2.4 on 2023-09-28 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=255)),
                ('Nacionalidade', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=255)),
                ('Localizacao', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data_Emprestimo', models.DateField()),
                ('Data_Devolucao', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=255)),
                ('Endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('Email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StatusLivro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=255)),
                ('Endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('Email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=255)),
                ('Ano_Publicacao', models.IntegerField(blank=True, null=True)),
                ('Sinopse', models.TextField(blank=True, null=True)),
                ('Editora_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.editora')),
                ('Status_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.statuslivro')),
            ],
        ),
        migrations.CreateModel(
            name='ListaDesejos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Livro_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.livro')),
                ('Usuario_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Exemplar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numero', models.IntegerField()),
                ('Disponibilidade', models.BooleanField(default=True)),
                ('Livro_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.livro')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo_Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emprestimo_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.emprestimo')),
                ('Usuario_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo_Exemplar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emprestimo_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.emprestimo')),
                ('Exemplar_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.exemplar')),
            ],
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='Usuario_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nota', models.IntegerField()),
                ('Comentario', models.TextField(blank=True, null=True)),
                ('Livro_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.livro')),
                ('Usuario_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
    ]
