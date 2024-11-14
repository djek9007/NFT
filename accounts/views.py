from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth import login


User = get_user_model()

# Регистрация пользователя
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            # Завершаем текущую сессию и начинаем новую для нового пользователя
            request.session.flush()
            login(request, user)  # Вход для нового пользователя
            
            return redirect('edit_profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Просмотр профиля
@login_required
def profile_view(request, user_id):
    # Получаем профиль пользователя по ID
    profile = get_object_or_404(Profile, user__id=user_id)
    return render(request, 'profile/business_card.html', {'profile': profile})

# Редактирование профиля
@login_required
def edit_profile(request):
    # Получаем профиль текущего пользователя
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # Сохраняем изменения профиля
            return redirect('profile', user_id=request.user.id)  # Перенаправление на профиль пользователя
    else:
        form = ProfileForm(instance=profile)  # Инициализация формы с данными текущего профиля

    return render(request, 'profile/profile.html', {'form': form})


# Кастомное представление для входа
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        # Перенаправление на профиль текущего пользователя после входа
        user_id = self.request.user.id
        return reverse_lazy('profile', kwargs={'user_id': user_id})

# Генерация vCard
# views.py
from django.http import HttpResponse
from .models import Profile

def generate_vcard(request):
    # Попробуем получить профиль текущего пользователя
    try:
        profile = Profile.objects.get(user=request.user)
        print("Profile data:", profile.first_name, profile.last_name, profile.email, profile.phone_number)
    except Profile.DoesNotExist:
        print("Profile does not exist.")
        return HttpResponse("Profile does not exist.", status=404)
    
    # Формируем данные vCard
    vcard_data = """
BEGIN:VCARD
VERSION:3.0
N:{last_name};{first_name};;;
FN:{first_name} {last_name}
EMAIL:{email}
TEL;TYPE=CELL:{phone_number}
PHOTO;VALUE=URI:{avatar_url}
X-WHATSAPP:{whatsapp_link}
X-TELEGRAM:{telegram_link}
X-TIKTOK:{tiktok_link}
END:VCARD
""".format(
        last_name=profile.last_name or 'No last name',
        first_name=profile.first_name or 'No first name',
        email=profile.email or 'No email',
        phone_number=profile.phone_number or 'No phone number',
        avatar_url=profile.avatar.url if profile.avatar else 'No avatar',
        whatsapp_link=profile.whatsapp_link or 'No WhatsApp',
        telegram_link=profile.telegram_link or 'No Telegram',
        tiktok_link=profile.tiktok_link or 'No TikTok',
    )
    
    # Выводим данные vCard в консоль для проверки
    print("Generated vCard data:\n", vcard_data) 

    # Создаем HTTP-ответ с данными vCard
    response = HttpResponse(vcard_data, content_type="text/vcard")
    response['Content-Disposition'] = 'attachment; filename="contact.vcf"'
    return response







