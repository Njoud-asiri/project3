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
    'accounts.apps.AccountsConfig',
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


# 🧩 إعدادات القوالب (Templates)
# لاحظي أن اسم المجلد هو "tempaltes" كما ذكرتِ بالضبط
TEMPLATES_DIR = BASE_DIR / 'tempaltes'  

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],  # 🔹 مسار القوالب
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# 🚀 إعداد تطبيق WSGI
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


# 🖼️ الملفات الثابتة (Static Files)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # مجلد static العام أثناء التطوير
STATIC_ROOT = BASE_DIR / 'staticfiles'    # مجلد التجميع النهائي للنشر


# 📸 ملفات الوسائط (Media Files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # مكان تخزين الملفات المرفوعة


# 🧱 الحقل الافتراضي للمفاتيح الأساسية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
