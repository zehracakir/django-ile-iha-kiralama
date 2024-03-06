from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import CustomUserSerializer, IhaSerializer, KiralamaSerializer
from .models import CustomUser, Iha, Kiralama

# Uye kaydi ve kayit konrtolu
class CustomUserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class CustomUserDetailAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

# Iha Ekleme ve Listeleme
class IhaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Iha.objects.all()
    serializer_class = IhaSerializer
    permission_classes = [permissions.IsAuthenticated]

# Iha Silme ve Guncelleme
class IhaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Iha.objects.all()
    serializer_class = IhaSerializer
    permission_classes = [permissions.IsAuthenticated]

# Kiralama İslemleri Ekleme ve Listeleme
class KiralamaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kiralama.objects.all()
    serializer_class = KiralamaSerializer
    permission_classes = [permissions.IsAuthenticated]

# Kiralama İslemleri Silme ve Guncelleme
class KiralamaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kiralama.objects.all()
    serializer_class = KiralamaSerializer
    permission_classes = [permissions.IsAuthenticated]

# Kiralanan İhalar Icin Kiralama Kayitlarını Getiren View
class KiralananIhalarAPIView(generics.ListAPIView):
    serializer_class = KiralamaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Kiralama.objects.filter(kiralayan_uye=user)

