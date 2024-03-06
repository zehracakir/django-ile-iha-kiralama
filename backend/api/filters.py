import django_filters
from .models import Iha, Kiralama

class IhaFilter(django_filters.FilterSet):
    marka = django_filters.CharFilter(lookup_expr='icontains')
    model = django_filters.CharFilter(lookup_expr='icontains')
    agirlik = django_filters.NumberFilter(lookup_expr='icontains')
    kategori = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Iha
        fields = ['marka', 'model', 'agirlik', 'kategori']

class KiralamaFilter(django_filters.FilterSet):
    iha_marka = django_filters.CharFilter(field_name='iha__marka', lookup_expr='icontains')
    iha_model = django_filters.CharFilter(field_name='iha__model', lookup_expr='icontains')
    kiralayan_uye = django_filters.CharFilter(field_name='kiralayan_uye__username', lookup_expr='icontains')

    class Meta:
        model = Kiralama
        fields = ['iha_marka', 'iha_model', 'kiralayan_uye']
