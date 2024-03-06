from django.urls import path
from api.views import CustomUserCreateAPIView, CustomUserDetailAPIView, IhaListCreateAPIView, IhaDetailAPIView, KiralamaListCreateAPIView, KiralamaDetailAPIView, KiralananIhalarAPIView
from django.contrib import admin
from django.views.generic import TemplateView
urlpatterns = [
    
    # Üye kaydı ve kayıt kontrolü
    path('register/', CustomUserCreateAPIView.as_view(), name='user-register'),
    path('user/<int:pk>/', CustomUserDetailAPIView.as_view(), name='user-detail'),

    # İha ekleme ve listeleme
    path('iha/', IhaListCreateAPIView.as_view(), name='iha-list-create'),
    path('iha/<int:pk>/', IhaDetailAPIView.as_view(), name='iha-detail'),

    # Kiralama işlemleri ekleme ve listeleme
    path('kiralama/', KiralamaListCreateAPIView.as_view(), name='kiralama-list-create'),
    path('kiralama/<int:pk>/', KiralamaDetailAPIView.as_view(), name='kiralama-detail'),

    # Kiralanan İhalar için Kiralama kayıtlarını getiren view
    path('kiralanan-ihalar/', KiralananIhalarAPIView.as_view(), name='kiralanan-ihalar-list'),

    #admin super
    path("admin/", admin.site.urls),
   
]
