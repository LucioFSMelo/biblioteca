# Generated by Django 4.1.7 on 2023-04-03 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='ano_edicao',
            field=models.CharField(max_length=50),
        ),
    ]
