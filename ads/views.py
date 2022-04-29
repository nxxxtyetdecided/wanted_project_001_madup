import json

from datetime import datetime
from django.http import HttpResponse, JsonResponse
from rest_framework import status

from .serializers import AdSerializer, ResultSerializer
from rest_framework.decorators import api_view

from ads.models import Ad, Result
from ads.serializers import AdSerializer

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

# 클릭당 코스트

@api_view(['GET'])
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

@api_view(['GET'])
def result_list(request):
    """
    류성훈
    """
    if request.method == 'GET':
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def result_detail(request, pk):
    """
    류성훈
    """
    try:
        result = Result.objects.get(id=pk)
    except Ad.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ResultSerializer(result)
        return JsonResponse(serializer.data)

@api_view(['PATCH', 'DELETE'])
def update_delete_ad(request, advertiser, uid):
    """
    권상현 / 정미정
    """
    if request.method == 'PATCH':
        """
        권상현
        """
        try:
            data = json.loads(request.body)
            ad = Ad.objects.get(user = advertiser, uid = uid)
            start_date = data.get('start_date', ad.start_date)
            end_date = data.get('end_date', ad.end_date)
            budget = data.get('budget', ad.budget)
            estimated_spend = data.get('estimated_spend', ad.estimated_spend)

            if start_date <= datetime.now().date():
                return JsonResponse({'MESSAGE': 'INVALID_DATE'}, status = 400)

            if start_date > end_date:
                return JsonResponse({'MESSAGE': 'INVALID_DATE'}, status = 400)

            if budget < 0 or estimated_spend < 0:
                return JsonResponse({'MESSAGE': 'INVALID_VALUE'}, status = 400)

            ad.start_date = start_date
            ad.end_date = end_date
            ad.budget = budget
            ad.estimated_spend = estimated_spend
            ad.save()

            return JsonResponse({'MESSAGE': 'SUCCESS'}, status = 200)
        
        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)

        except Ad.DoesNotExist:
            return JsonResponse({'MESSAGE':'AD_DOES_NOT_EXIST'}, status = 404)

    elif request.method == 'DELETE':
        """
                    정미정 (soft delete로 구현)
                """
        try:
            ad = Ad.objects.get(uid=uid)
            serializer = AdSerializer(ad)
            ad.delete_at = datetime.now()
            ad.is_delete = True
            ad.save()
            return JsonResponse(status=status.HTTP_201_CREATED, data=serializer.data)
        except Ad.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

