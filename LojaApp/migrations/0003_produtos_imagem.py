# Generated by Django 5.0.6 on 2024-06-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LojaApp', '0002_remove_produtos_dataval_vendas'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='imagem',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='img_produto/'),
        ),
    ]
