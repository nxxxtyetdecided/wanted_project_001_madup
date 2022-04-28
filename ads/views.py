from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Ad ,Result
from .serializers import AdSerializer,ResultSerializer
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


@api_view(['POST','GET','DELETE'])
def get_create_ad(request):
    """
    김석재
    """
    print(request.method)
    # ad=Ad()
    # result=Result()
    #(필수) media, start date, end date (기간)
    #(선택) budget (집행 예산), estimated_spend(일일 집행 예산), location (집행 지역), kpi(목표치)
    if request.method == 'GET':        
        ads = Ad.objects.last()
        res = Result.objects.last()
        res1 = Result.objects.filter(id=5)
        serializer = AdSerializer(ads)#, many=True)
        serializer1 = ResultSerializer(res)
        serializer2 = ResultSerializer(res1 ,many=True)

        return Response(serializer1.data)
    
    #테스트 중인데 POST를 인식을 못한다 홀리.. DELETE도 인식안됨
    elif request.method == 'POST':        
        print(request.POST)
        # ad.start_date = request.data['start_date']
        # ad.end_date = request.data['end_date']     
        # ad.save()
        # result.ad = ad.uid
        # result.media = request.data['media']
        # result.save()
        #serializer = AdSerializer(ad)
        
        ads = Ad.objects.last()
        serializer1 = AdSerializer(ads)#, many=True)
        return Response(serializer1.data)
    
    


@api_view(['PATCH', 'DELETE'])
def update_delete_ad(request):
    if request.method == 'PATCH':
        pass


    elif request.method == 'DELETE':
        pass
