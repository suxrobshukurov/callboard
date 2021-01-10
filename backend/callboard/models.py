from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Категории"""
    name = models.CharField('Имя', max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    slug = models.SlugField('url', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

class FilterAdvert(models.Model):
    """Фильтры"""
    name = models.CharField('Имя', max_length=50, unique=True)
    slug = models.SlugField('url', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        verbose_name = 'Фильтр'
        verbose_name_plural = "Фильтры"

class DateAdvert(models.Model):
    """Срок для объявления"""
    name = models.CharField('Имя', max_length=50, unique=True)
    slug = models.SlugField('url', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        verbose_name = 'Фильтр'
        verbose_name_plural = "Фильтры"

class Advert(models.Model):
    """Объявленмя"""

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    filters = models.ForeignKey(FilterAdvert, verbose_name='Срок', on_delete=models.CASCADE)
    date = models.ForeignKey(DateAdvert, verbose_name='Фильтр', on_delete=models.CASCADE)
    subject = models.CharField('Тема', max_length=200)
    description = models.TextField('Объявления', max_length=700)
    images = models.ForeignKey(
        'gallery.Gallery',
        verbose_name='Изображения',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    file = models.FileField('Файл', upload_to='callboard_file/', blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    moderation = models.BooleanField('Модерация', default=False)
    # TODO: для slug генерировать путь (id, subject)
    slug = models.SlugField('url', max_length=200, unique=True)

    def __str__(self):
        return self.subject

    class MPTTMeta:
        verbose_name = 'Объявление'
        verbose_name_plural = "Объявления"



