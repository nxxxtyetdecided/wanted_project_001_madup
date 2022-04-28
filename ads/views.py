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
    류성훈
    모든 광고들의 정보를 조회합니다.
    """
    if request.method == 'GET':
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def ad_detail(request, pk):
    """
    류성훈
    """
    try:
        ad = Ad.objects.get(uid=pk)
    except Ad.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AdSerializer(ad)
        return JsonResponse(serializer.data)