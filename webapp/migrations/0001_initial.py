# Generated by Django 4.1 on 2022-08-27 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('name', models.CharField(max_length=35, verbose_name='Название продукта')),
                ('category', models.CharField(choices=[('Drinks', 'Напитки'), ('Sweets', 'Сладости'), ('Bakery', 'Выпечка')], default='Drinks', max_length=45, verbose_name='Категория продукта')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание продукта')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('review_text', models.TextField(max_length=3000, verbose_name='Отзыв')),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=1, verbose_name='Оценка продукта')),
                ('review_status', models.BooleanField(default=False)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='webapp.product', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'db_table': 'review',
            },
        ),
    ]
