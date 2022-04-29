import json

from datetime import datetime,timedelta
from django.db.models import Sum, F, Value
from django.http import HttpResponse, JsonResponse
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AdSerializer, ResultSerializer

from ads.models import Ad, Result
from ads.serializers import AdSerializer

from datetime import datetime
import math


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

@api_view(['GET'])
def get_result(request):
    """
    류성훈
    """
    # 광고주의 id 받아오기
    advertiser_id = request.GET.get('advertiser', None)
    print("광고주 advertiser:",advertiser_id)
    
    try:
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
    except TypeError:
        return Response("타입이 잘못되었습니다.", status=404)

    # 광고주의 광고들을 불러옵니다.
    advertiser = Ad.objects.filter(advertiser=advertiser_id)
    if not advertiser:
        return Response("존재하지 않는 광고주 id입니다.", status=404)
    
    advertiser_uid = advertiser.values('uid')
    print('advertiser_uid:',advertiser_uid)
    

    # i. CTR = click * 100 / impression
    # ii. ROAS = cv * 100 / cost
    # iii. CPC = cost / click
    # iv. CVR = conversion * 100 / click
    # v. CPA = cost / conversion
    
    media_list = ['naver', 'facebook', 'google', 'kekeo']
    
    answer = {}
    for media in media_list:
        objs = Result.objects.filter(uid__in=advertiser_uid, date__gte=start_date, date__lte=end_date, media=media)
        if objs:
            total = objs.aggregate(
                total_click=Sum('click'),
                total_impression = Sum('impression'),
                total_cost = Sum('cost'),
                total_conversion = Sum('conversion'),
                total_cv = Sum('cv'),
                )
            val = {
                'ctr': math.trunc((total['total_click'] * 10000 / total['total_impression']))/100,
                'roas': math.trunc(total['total_cv'] * 10000 / total['total_cost'])/100,
                'cpc': math.trunc(total['total_cost'] * 100 / total['total_click'])/100,
                'cvr': math.trunc(total['total_conversion'] * 10000 / total['total_click'])/100,
                'cpa': math.trunc(total['total_cost'] * 100 / total['total_conversion'])/100,
            }

            answer[media] = val

    return Response(answer, status=200)


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
        
        #end-start day로 차이나는 값 만큼 result를 생성 (최소1)
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end   = datetime.strptime(end_date, '%Y-%m-%d')
        day   = end - start 
        
        if start < datetime.now():
            return Response({'MESSAGE': 'INVALID_DATE'}, status = 400)
        if start >= end:
            return Response({'MESSAGE': 'INVALID_DATE'}, status = 400)
        

        
        new_ad = Ad.objects.create(
            start_date    = start_date,
            end_date      = end_date,
            advertiser_id = advertiser_id,
            uid           = uid
        )
        
        #필수 데이터 외에 추가데이터
        if 'budget' in request.data:
            new_ad.budget = request.data['budget']
            if float(request.data['budget']) < 0:
                return Response({'MESSAGE': 'INVALID_VALUE'}, status = 400)
            
        if 'estimated_spend' in request.data:
            new_ad.estimated_spend = request.data['estimated_spend']
            if float(request.data['estimated_spend']) < 0:
                return Response({'MESSAGE': 'INVALID_VALUE'}, status = 400)
        
        for day in range(day.days+1):
            date = start + timedelta(days=day)
            Result.objects.create(
                ad = new_ad,
                media = media,
                date = date
            )

        serializer = AdSerializer(new_ad)
        return Response(serializer.data)
    
    #POST가 아닐때
    else :
        return Response({'MESSAGE': 'Method Not Allowed'}, status = 405)
        


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
            ad = Ad.objects.get(advertiser = advertiser, uid = uid)
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
            return JsonResponse({'MESSAGE': 'SUCCESS'}, status=status.HTTP_201_CREATED, data=serializer.data)

        except Ad.DoesNotExist:
            return JsonResponse({'MESSAGE': 'AD_DOES_NOT_EXIST'}, status=status.HTTP_404_NOT_FOUND)

