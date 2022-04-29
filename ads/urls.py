from django.urls import path
from ads import views


urlpatterns = [
    path('', views.get_result),
    path('list/',views.ad_list),
    #path('<str:pk>', views.ad_detail),
    path('result', views.result_list),
    path('result/<str:pk>', views.result_detail),
    path('',views.get_create_ad),
    path('<str:pk>/', views.ad_detail),
    path('<str:advertiser>/<str:uid>', views.update_delete_ad)
]

