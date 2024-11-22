from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import generate_vcard

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),  # Маршрут для просмотра профиля с user_id
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Используем кастомное представление входа
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('generate_vcard/', generate_vcard, name='generate_vcard'),
    path('generate_vcard/<int:user_id>/', views.generate_vcard, name='generate_vcard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    
    
