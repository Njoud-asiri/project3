from django.contrib import admin
from .models import UserProfile

# تسجيل نموذج المستخدم في لوحة التحكم
admin.site.register(UserProfile)
