# Generated by Django 4.0.1 on 2022-01-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0006_filme_em_breve'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmeBreve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('imagem_font', models.TextField()),
                ('data_lancamento', models.CharField(max_length=10)),
            ],
        ),
    ]
