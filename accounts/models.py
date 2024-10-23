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

    whatsapp_link = models.URLField(max_length=200, blank=True, null=True)
    telegram_link = models.URLField(max_length=200, blank=True, null=True)
    tiktok_link = models.URLField(max_length=200, blank=True, null=True)

    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Генерация QR-кода на основе URL профиля
        qr_data = f"http://127.0.0.1:8000/accounts/profile/{self.id}/"  # Можно заменить на реальный URL
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        # Сохранение изображения QR-кода
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        filename = f'qr_code_{self.user.username}.png'
        self.qr_code.save(filename, File(buffer), save=False)

        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.user.username
