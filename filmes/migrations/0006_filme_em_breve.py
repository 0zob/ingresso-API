# Generated by Django 4.0.1 on 2022-01-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0005_noticia'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='em_breve',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]