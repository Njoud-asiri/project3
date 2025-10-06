# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    اسم_المنتج = models.CharField(max_length=100, verbose_name=_('اسم المنتج'))
    السعر = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('السعر'))
    تاريخ_الإضافة = models.DateTimeField(auto_now_add=True, verbose_name=_('تاريخ الإضافة'))

    class Meta:
        verbose_name = _('المنتج')            # اسم المفرد بالعربية في لوحة التحكم
        verbose_name_plural = _('المنتجات')   # اسم الجمع بالعربية في لوحة التحكم

    def __str__(self):
        return self.اسم_المنتج
