from django.db import models


# Модель для типов
class Type(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


# Модель для категорий
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', unique=True, blank=False)
    type = models.ForeignKey(
        'Type',
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name='Category',
        verbose_name='Тип'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Модель для подкатегорий
class Subcategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', unique=True, blank=False)
    parent = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name='subcategories',
        verbose_name='Категория'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


# Модель для статусов
class Status(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


# Модель для записей
class Record(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    date = models.DateField(verbose_name='Дата')
    amount = models.IntegerField(blank=False, verbose_name='Сумма')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    subcategory = models.ForeignKey(
        'Subcategory',
        on_delete=models.CASCADE,
        related_name='records',
        verbose_name='Подкатегория',
        blank=False
    )
    status = models.ForeignKey(
        'Status',
        on_delete=models.PROTECT,
        verbose_name='Статус',
        blank=False
    )

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.name
