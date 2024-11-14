from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from django.core.files import File
import qrcode

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # Поля для WhatsApp и Telegram, принимают только цифры и символ +
    whatsapp_link = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[RegexValidator(r'^\+?\d+$', 'Введите только цифры и, при необходимости, знак + в начале для WhatsApp.')]
    )
    telegram_link = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[RegexValidator(r'^\+?\d+$', 'Введите только цифры и, при необходимости, знак + в начале для Telegram.')]
    )
    
    # Поле для TikTok, принимает только латинские буквы и цифры
    tiktok_link = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        validators=[RegexValidator(r'^[A-Za-z0-9]+$', 'Введите только латинские буквы и цифры для TikTok.')]
    )

    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Генерация QR-кода на основе URL профиля
        qr_data = f"http://127.0.0.1:8080/accounts/profile/{self.id}/"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        filename = f'qr_code_{self.user.username}.png'
        self.qr_code.save(filename, File(buffer), save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
