from django.urls import path
from . import views

urlpatterns = [
    # เพิ่ม URL สำหรับหน้าค้นหาวิชา
    path('search/', views.search_course, name='search_course'),
]
