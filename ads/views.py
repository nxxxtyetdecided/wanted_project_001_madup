from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Ad
from .serializers import AdSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def ad_list(request):
    """
    류성훈
    모든 광고들의 정보를 조회합니다.
    """
    if request.method == 'GET':
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def ad_detail(request, pk):
    """
    류성훈
    """
    try:
        ad = Ad.objects.get(uid=pk)
        print(ad)
    except Ad.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AdSerializer(ad)
        return JsonResponse(serializer.data)
from django.shortcuts import render
from rest_framework.decorators import api_view


@api_view(['PATCH', 'DELETE'])
def update_delete_ad(request):
    if request.method == 'PATCH':
        pass


    elif request.method == 'DELETE':
        pass
