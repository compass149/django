from django.urls import path
from . import views

app_name = 'intro'  
urlpatterns = [
    path('', views.index, name='index'),        # 메인 페이지
    path('member/', views.member, name='member'),  # 팀원 소개 페이지
    path('data_source/', views.data_source, name='data_source'),  # 데이터 소개 페이지
    path('data_processing/', views.data_processing, name='data_processing'),  # 데이터 소개 페이지
    path('chart/', views.chart, name='chart'),  # 데이터 소개 페이지
    path('conclusion/', views.conclusion, name='conclusion'),  # 데이터 소개 페이지
]
