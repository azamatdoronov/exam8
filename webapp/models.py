from django.contrib.auth import get_user_model
from django.db import models

CATEGORY_CHOICES = [('Drinks', 'Напитки'), ('Sweets', 'Сладости'), ('Bakery', 'Выпечка')]
RATING_CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(max_length=35, null=False, blank=False, verbose_name="Название продукта")
    category = models.CharField(max_length=45, null=False, blank=False, choices=CATEGORY_CHOICES,
                                default=CATEGORY_CHOICES[0][0],
                                verbose_name='Категория продукта')
    description = models.TextField(max_length=3000, verbose_name="Описание продукта")
    image = models.ImageField(upload_to='images', null=True, blank=True,
                              verbose_name="Изображение")

    def __str__(self):
        return f"{self.id}. {self.name}."

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
            ('create_product', 'Создать товар'),
            ('update_product', 'Редактировать товар'),
            ('remove_product', 'Удалить товар'),
        ]


class Review(BaseModel):
    author = models.ForeignKey(get_user_model(), related_name="reviews", verbose_name="Автор", default=1,
                               on_delete=models.SET_DEFAULT)
    product = models.ForeignKey("webapp.Product", on_delete=models.CASCADE, related_name="products",
                                verbose_name="Продукт")
    review_text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Отзыв")
    rating = models.CharField(max_length=1, null=False, blank=False, choices=RATING_CHOICES,
                              default=RATING_CHOICES[0][0],
                              verbose_name="Оценка продукта")
    review_status = models.BooleanField(default=False)

    def str(self):
        return f"{self.id}. {self.author}"

    class Meta:
        db_table = "review"
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        permissions = [
            ('create_review', 'Создать отзыв'),
            ('update_review', 'Редактировать отзыв'),
            ('remove_review', 'Удалить отзыв'),
        ]