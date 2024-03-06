from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


#Iha icin marka, model, agirlik, kategori 
class Iha(models.Model):
    marka = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    agirlik = models.FloatField()
    kategori = models.CharField(max_length=30)

# AbstractUser sinifindan CustomUser'ı turettim.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(
        Permission, related_name='customuser_user_permissions'
    )
    def save(self, *args, **kwargs):
        if not self.id:
            self.password = make_password(self.password)
        super(CustomUser, self).save(*args, **kwargs)

# Kiralama icin iha, tarih ve saat, kiralayan uye bilgileri
class Kiralama(models.Model):
    iha = models.ForeignKey('Iha', on_delete=models.SET_NULL, null=True)
    kiralayan_uye = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    kiralama_saati = models.DateTimeField()
    kiralama_bitis_saati = models.DateTimeField()

# Kullanicilarin kiraladiklari iha bilgilerini tutmak icin ekledim
class UserDetay(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_detay', null=True)
    ihalar = models.ManyToManyField('Iha', related_name='kiralanan_ihalar', blank=True)
    