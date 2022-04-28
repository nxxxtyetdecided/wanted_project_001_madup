from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Ad
from .serializers import AdSerializer

# Create your views here.
class AdViewSet(viewsets.ViewSet):
    """
    A viewset for viewing and editing article instances.
    """
    # serializer_class = ArticleSerializer
    # queryset = Article.objects.all()
    def list(self, request):
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = Ad.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = AdSerializer(article)
        return Response(serializer.data)


@csrf_exempt
def ad_list(request):
    """
    List all code ads
    """
    if request.method == 'GET':
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return JsonResponse(serializer.data, safe=False)