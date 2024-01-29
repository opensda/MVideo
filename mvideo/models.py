from django.db import models

NULLABLE = {"null": True, "blank": True}

class NetworkUnit(models.Model):
    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )

    name = models.CharField(max_length=255, verbose_name='название', **NULLABLE)
    email = models.EmailField(verbose_name='почта', **NULLABLE)
    country = models.CharField(max_length=255, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=255, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=255, verbose_name='улица', **NULLABLE)
    house_number = models.CharField(max_length=10, verbose_name='номер дома', **NULLABLE)
    supplier = models.ForeignKey('self', verbose_name='поставщик',
                                 on_delete=models.SET_NULL,
                                 related_name='suppliers',
                                 **NULLABLE)
    level = models.PositiveIntegerField(choices=LEVEL_CHOICES, verbose_name='уровень', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)
    debt_to_supplier = models.DecimalField(max_digits=10,
                                           decimal_places=2,
                                           default=0,
                                           verbose_name='задолженность перед поставщиком',
                                           **NULLABLE)

    class Meta:
        verbose_name = 'элемент сети'
        verbose_name_plural = 'элементы сети'

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='продукт', **NULLABLE)
    model = models.CharField(max_length=255, verbose_name='модель', **NULLABLE)
    release_date = models.DateField(verbose_name='дата выхода на рынок', **NULLABLE)
    owner = models.ForeignKey(NetworkUnit,
                              on_delete=models.CASCADE,
                              verbose_name='владелец продукта')



    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.name


