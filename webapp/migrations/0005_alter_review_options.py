# Generated by Django 4.1 on 2022-08-27 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'permissions': [('create_review', 'Создать отзыв'), ('update_review', 'Редактировать отзыв'), ('remove_review', 'Удалить отзыв')], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
