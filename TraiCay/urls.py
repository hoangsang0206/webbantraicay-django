from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='TrangChu'),
    path('home/', views.home, name='TrangChu'),
    path('loai/<str:id>', views.loc_theo_loai, name='LocTheoLoai'),
    path('timkiem/', views.tim_kiem, name='TimKiem'),
    path('sanpham/<str:id>', views.sanpham, name='SanPham'),

    path('api/loai/', views.getLoai, name='GetLoai'),
    path('api/timkiem/', views.getTimKiem, name='GetTimKiem'),
]