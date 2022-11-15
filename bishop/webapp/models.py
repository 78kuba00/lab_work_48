from django.db import models
STATUS_CHOICES = [('other', 'Other'), ('electronics', 'Electronics'), ('garden', 'Garden'), ('food', 'Food')]

class Product(models.Model):
    product = models.CharField(max_length=100, null=False, blank=False, verbose_name="Наименование товара")
    details = models.TextField(max_length=2000, null=True, blank=True, default="-", verbose_name="Описание товара")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name="Статус")
    balance = models.PositiveIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)


    def __str__(self):
        return f'{self.id}. {self.product}'