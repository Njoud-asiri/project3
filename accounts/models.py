# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    اسم_المستخدم = models.CharField(max_length=100, verbose_name=_('اسم المستخدم'))
    البريد_الإلكتروني = models.EmailField(unique=True, verbose_name=_('البريد الإلكتروني'))
    تاريخ_الانضمام = models.DateTimeField(auto_now_add=True, verbose_name=_('تاريخ الانضمام'))

    class Meta:
        verbose_name = _('المستخدم')
        verbose_name_plural = _('المستخدمون')

    def __str__(self):
        return self.اسم_المستخدم
