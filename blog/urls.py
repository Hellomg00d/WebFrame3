from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),#아무것도 없으면 뷰의 인덱스를 참고해라
    path('<int:pk>/', views.single_post_page),
]