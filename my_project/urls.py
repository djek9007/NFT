from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Подключаем стандартные маршруты авторизации
    path('', lambda request: redirect('login')),  # Перенаправляем главную страницу на логин
]
