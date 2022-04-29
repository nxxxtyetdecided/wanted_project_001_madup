from django.urls import path

from ads         import views


urlpatterns = [
    path('result/', views.get_result),
    path('', views.post_create_ad),
    path('<str:advertiser>/<str:uid>', views.update_delete_ad)
]

