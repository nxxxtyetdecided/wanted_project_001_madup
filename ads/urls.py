from django.urls import path, include

from ads.models import Ad
from ads import views
#GenericAPIView
#ArticleAPIView, ArticleDetails
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('advertise', views.ad_list),
    path('advertise/<str:pk>', views.ad_detail),
    path('result', views.result_list),
    path('result/<int:pk>', views.result_detail),

]

