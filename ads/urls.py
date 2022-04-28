from django.urls import path
from ads import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('advertise', views.ad_list),
    path('advertise/<str:pk>', views.ad_detail),
    path('result', views.result_list),
    path('result/<str:pk>', views.result_detail),
    path('',views.get_create_ad),
    path('<str:pk>/', views.ad_detail),
    path('<str:advertiser>/<str:uid>', views.update_delete_ad)
]

