# Generated by Django 4.1 on 2022-08-27 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_review_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('create_product', 'Создать товар'), ('update_product', 'Редактировать товар'), ('remove_product', 'Удалить товар')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
