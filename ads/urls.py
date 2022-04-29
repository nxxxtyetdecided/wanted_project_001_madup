from django.urls import path
from ads import views


urlpatterns = [
    path('', views.get_result),
    path('a',views.get_create_ad),
    path('<str:advertiser>/<str:uid>', views.update_delete_ad)
]

