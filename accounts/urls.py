from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
]
