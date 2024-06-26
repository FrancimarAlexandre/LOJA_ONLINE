# Generated by Django 5.0.6 on 2024-06-24 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LojaApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='dataVal',
        ),
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('valorTotal', models.FloatField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LojaApp.produtos')),
            ],
        ),
    ]
