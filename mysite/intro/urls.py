from django.urls import path
from . import views

app_name = 'intro'  
urlpatterns = [
    path('', views.index, name='index'),        # 메인 페이지
    path('member/', views.member, name='member'),  # 팀원 소개 페이지
]
