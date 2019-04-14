"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# BASE_DIR 等于 工程demo的目录
# 根路径:
# __file__: settings.py
# os.path.abspath(__file__): /Users/meihao/Destop/demo/demo/settings.py
# os.path.dirname(os.path.abspath(__file__)): /Users/meihao/Destop/demo/demo
# BASE_DIR =: /Users/meihao/Destop/demo

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# 秘钥加密
SECRET_KEY = '=9g_-nx6%-3k*q()+g9hu%-$xocel0bm=7dnf8gp4fy72fcn)8'

# 调试模式 ：true ,项目上线时关闭
DEBUG = True

# 白名单
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = []


# Application definition
# 已经安装的应用配置
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 配置的目的：使用当前的子应用能进行数据迁移
    # 将子应用的配置信息文件apps.py中的Config类添加到INSTALLED_APPS列表中。
    'users.apps.UsersConfig',
    'reuest.apps.ReuestConfig',
    'response.apps.ResponseConfig',
    'cook.apps.CookConfig',
    'session.apps.SessionConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 可以发送请求体数据的请求方式有 POST、PUT、PATCH、DELETE。
# Django默认开启了CSRF防护，会对上述请求方式进行CSRF防护验证，在测试时可以关闭CSRF防护机制，方法为在settings.py文件中注释掉CSRF中间件
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'demo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# LANGUAGE_CODE = 'en-us'
# 改中文 ：zh-hans
LANGUAGE_CODE = 'zh-hans'

# 时区：Asia/shanghai
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# 这个参数默认存在
STATIC_URL = '/static/'

# 我们可以添加这个参数, 用于补全静态文件路径
STATICFILES_DIRS = [
    # 拼接路径
    os.path.join(BASE_DIR, 'static')

]

# session存储方式配置
CACHES = {
    "default": {
        # 指定session存储
        "BACKEND": "django_redis.cache.RedisCache",
        # 定义django中redis的位置
        "LOCATION": "redis://192.168.56.134:6379/1",
        "OPTIONS": {
            # django使用redis的默认客户端来进行操作.
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
# 我们定义一个cache(本地缓存来存储信息,cahe指定的是redis)
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 本地的session使用的本地缓存名称是'default', 这个名称就是上面我们配置的caches的名
# 称"default"
SESSION_CACHE_ALIAS = "default"
