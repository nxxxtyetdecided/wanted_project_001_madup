from django.urls import path, include

from ads.models import Ad
from ads import views
#GenericAPIView
#ArticleAPIView, ArticleDetails
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.ad_list),
    path('<str:pk>/', views.ad_detail),
]

