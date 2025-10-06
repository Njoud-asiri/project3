# -*- coding: utf-8 -*-
from pathlib import Path

# 📂 المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔑 مفتاح الأمان (⚠️ لا تستخدمي هذا في بيئة الإنتاج)
SECRET_KEY = 'django-insecure-s_d8-i*vja6ix4mw3slznklxl@g##n*bpx4!jswabgcp8sepcz'

# ⚙️ وضع التصحيح (في بيئة الإنتاج اجعليه False)
DEBUG = True

# 🌐 المضيفون المسموح لهم (ضيفي نطاق موقعك عند رفع المشروع)
ALLOWED_HOSTS = []


# 🧩 التطبيقات المثبتة
INSTALLED_APPS = [
    # تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع الخاصة
    'accounts.apps.AccountsConfig',  # لضمان ظهور الاسم بالعربية
    'products.apps.ProductsConfig',
]


# 🧱 الوسائط (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # لدعم اللغة العربية
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ⚙️ إعدادات المشروع العامة
ROOT_URLCONF = 'project3.urls'

# 🧩 تعريف مسار القوالب (templates)
TEMPLATES_DIR = BASE_DIR / 'templates'  # مجلد القوالب في جذر المشروع

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],  # 🔹 هنا تمت إضافة مسار القوالب
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project3.wsgi.application'


# 🗄️ قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 🔐 التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# 🌍 الإعدادات الإقليمية واللغة
LANGUAGE_CODE = 'ar'           # اللغة العربية
TIME_ZONE = 'Asia/Riyadh'      # المنطقة الزمنية: الرياض
USE_I18N = True
USE_L10N = True
USE_TZ = True


# 🖼️ الملفات الثابتة (CSS, JS, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # تعريف مجلد static العام

# 🧱 الحقل الافتراضي للمفاتيح الأساسية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
