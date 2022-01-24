# Generated by Django 4.0.1 on 2022-01-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_filme', models.CharField(max_length=255)),
                ('imagem_font', models.TextField()),
                ('em_alta', models.BooleanField(default=False)),
                ('em_cartaz', models.BooleanField(default=False)),
                ('principal', models.BooleanField(default=False)),
                ('principal_imagem_font', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FilmeBreve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('imagem_font', models.TextField()),
                ('data_lancamento', models.CharField(blank=True, default=None, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('imagem', models.TextField()),
            ],
        ),
    ]
