# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from products import views as product_views  # ✅ استدعاء الفيو من تطبيق products
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 🏠 الصفحة الرئيسية
    path('', product_views.home, name='home'),
    
    # 👥 تطبيق الحسابات
    path('accounts/', include('accounts.urls')),
    
    # 🛒 تطبيق المنتجات
    path('products/', include('products.urls')),
]

# ✅ إعداد عرض ملفات الميديا أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
