from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'avatar', 'whatsapp_link', 'telegram_link', 'tiktok_link']

def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # Если профиль уже существует и QR-код сгенерирован, отображаем его
        if self.instance.pk and self.instance.qr_code:
            self.fields['qr_code'] = forms.ImageField(label='QR Code', required=False, widget=forms.ClearableFileInput(attrs={'readonly': 'readonly'}))