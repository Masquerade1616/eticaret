from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('urun/<int:urunId>', urun, name='urun'),
    path('ucuz/', ucuz, name='ucuz'),
    path('olustur/', olustur, name='olustur'),
    path('alisveris/', alisveris, name='alisveris'),
]