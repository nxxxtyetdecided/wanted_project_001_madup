import json

from datetime import datetime,timedelta
from django.http import HttpResponse, JsonResponse
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AdSerializer, ResultSerializer

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

#다른 코드가 정리되면 GET은 삭제하고 URL을 변경할 예정입니다
@api_view(['POST'])
def get_create_ad(request):    
    """
    김석재
    """
        
    # 필수 입력값 4개(ad) + 1개 (result) 입력시 ad를 하나(캠페인)생성 , 기간에 따라 하루마다 하나씩 result를 생성
    if request.method == 'POST':

        start_date    = request.data['start_date']
        end_date      = request.data['end_date']
        advertiser_id = request.data['advertiser_id']
        media         = request.data['media']
        uid           = request.data['uid']       
        
        if not start_date or not end_date or not advertiser_id or not media or not uid:
            return Response({'MESSAGE': 'MISSING_VALUE'}, status = 400)
        
        #end-start day로 차이나는 값 만큼 result를 생성 (최소1)
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end   = datetime.strptime(end_date, '%Y-%m-%d')
        day   = end - start 
        
        if start < datetime.now():
            return Response({'MESSAGE': 'INVALID_DATE'}, status = 400)
        if start >= end:
            return Response({'MESSAGE': 'INVALID_DATE'}, status = 400)
        

        
        new_ad = Ad.objects.create(
            start_date = start_date,
            end_date   = end_date,
            advertiser_id = advertiser_id,
            uid        = uid
        )
        
        #필수 데이터 외에 추가데이터
        if 'budget' in request.data:
            new_ad.budget          = request.data['budget']
            if float(request.data['budget']) < 0:
                return Response({'MESSAGE': 'INVALID_VALUE'}, status = 400)
            
        if 'estimated_spend' in request.data:
            new_ad.estimated_spend = request.data['estimated_spend']
            if float(request.data['estimated_spend']) < 0:
                return Response({'MESSAGE': 'INVALID_VALUE'}, status = 400)
        
        for day in range(day.days+1):
            date = start + timedelta(days=day)
            Result.objects.create(
                uid   = new_ad,
                media = media,
                date  = date
            )

        serializer = AdSerializer(new_ad)
        return Response(serializer.data)
   
        


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

            start_date = datetime.strptime(str(data['start_date']), '%Y-%m-%d').date(),
            end_date = datetime.strptime(str(data['end_date']), '%Y-%m-%d').date(),
            budget = data['budget']
            estimated_spend = data['estimated_spend']

            if start_date <= datetime.now().date():
                return JsonResponse({'MESSAGE': 'INVALID_DATE'}, status = 400)

            if start_date >= end_date:
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
        print(uid)
        try:
            ad = Ad.objects.get(uid=uid)
            serializer = AdSerializer(ad)
            ad.delete_at = datetime.now()
            ad.is_delete = True
            ad.save()
            return JsonResponse(status=status.HTTP_201_CREATED, data=serializer.data)
        except Ad.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

