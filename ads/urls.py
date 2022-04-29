from django.urls import path
from ads import views


urlpatterns = [
<<<<<<< HEAD
    path('aa', views.ad_list),
=======
    path('', views.ad_list),
>>>>>>> 825ee988ae643e8bca14e2868961bb05df86dd0e
    path('<str:pk>', views.ad_detail),
    path('result', views.result_list),
    path('result/<str:pk>', views.result_detail),
    path('',views.get_create_ad),
    path('<str:pk>/', views.ad_detail),
    path('<str:advertiser>/<str:uid>', views.update_delete_ad)
]

