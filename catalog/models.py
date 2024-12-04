from django.db import models


class Candles(models.Model):
    """Модель для описания свечей"""
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name='Описание')
    type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Тип свечи')
    manufacturer = models.CharField(max_length=200, blank=True, null=True, verbose_name='Производитель')
    size = models.CharField(max_length=200, blank=True, null=True, verbose_name='Размер свечи')
    diameter = models.CharField(max_length=200, blank=True, null=True, verbose_name='Диаметр свечи')
    length = models.CharField(max_length=200, blank=True, null=True, verbose_name='Длинна свечи')
    quantity = models.CharField(max_length=200, blank=True, null=True, verbose_name='Количество свечей')
    burning_time = models.CharField(max_length=200, blank=True, null=True, verbose_name='Время горения')
    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Изображение')
    price = models.CharField(max_length=200, blank=True, null=True, verbose_name='Цена')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Свеча'
        verbose_name_plural = 'Свечи'
        ordering = ['price']
        #permissions =
