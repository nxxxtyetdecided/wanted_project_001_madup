import json
import math

from datetime                  import datetime,timedelta
from django.db.models          import Sum
from django.http               import JsonResponse
from rest_framework            import status
from rest_framework.response   import Response
from rest_framework.decorators import api_view

from ads.models      import Ad, Result
from ads.serializers import AdSerializer


@api_view(['GET'])
def get_result(request):
    """
    류성훈
    """
    # 광고주의 id 받아오기
    advertiser_id = request.GET.get('advertiser', None)
    
    try:
        start_date = request.GET.get('start_date', None)
        end_date   = request.GET.get('end_date', None)
    except TypeError:
        return Response("타입이 잘못되었습니다.", status=404)

    # 광고주의 광고들을 불러옵니다.
    advertiser = Ad.objects.filter(advertiser=advertiser_id, is_delete=False)
    if not advertiser:
        return Response("존재하지 않는 광고주 id입니다.", status=404)
    
    advertiser_uid = advertiser.values('uid')
    
    media_list = ['naver', 'facebook', 'google', 'kekeo']
    
    answer = {}
    for media in media_list:
        objs = Result.objects.filter(uid__in=advertiser_uid, date__gte=start_date, date__lte=end_date, media=media)
        if objs:
            total = objs.aggregate(
                total_click      =Sum('click'),
                total_impression = Sum('impression'),
                total_cost       = Sum('cost'),
                total_conversion = Sum('conversion'),
                total_cv = Sum('cv'),
            )

            val = {
                'ctr' : 0 if total['total_impression']==0 else math.trunc((total['total_click'] * 10000 / total['total_impression']))/100,
                'roas': 0 if total['total_cost']==0 else math.trunc(total['total_cv'] * 10000 / total['total_cost'])/100,
                'cpc' : 0 if total['total_click']==0 else math.trunc(total['total_cost'] * 100 / total['total_click'])/100,
                'cvr' : 0 if total['total_click']==0 else math.trunc(total['total_conversion'] * 10000 / total['total_click'])/100,
                'cpa' : 0 if total['total_conversion']==0 else math.trunc(total['total_cost'] * 100 / total['total_conversion'])/100,
            }

            answer[media] = val

    return Response(answer, status=200)


@api_view(['POST'])
def post_create_ad(request):    
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
            return Response({'MESSAGE' : 'MISSING_VALUE'}, status = 400)
        
        #end-start day로 차이나는 값 만큼 result를 생성 (최소1)
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end   = datetime.strptime(end_date, '%Y-%m-%d')
        day   = end - start 
        
        if start < datetime.now():
            return Response({'MESSAGE' : 'INVALID_DATE'}, status = 400)
        if start >= end:
            return Response({'MESSAGE' : 'INVALID_DATE'}, status = 400)
        
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
                return Response({'MESSAGE' : 'INVALID_VALUE'}, status = 400)
            
        if 'estimated_spend' in request.data:
            new_ad.estimated_spend = request.data['estimated_spend']
            if float(request.data['estimated_spend']) < 0:
                return Response({'MESSAGE' : 'INVALID_VALUE'}, status = 400)
        
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
            ad = Ad.objects.get(advertiser = advertiser, uid = uid)

            if ad.is_delete == True:
                raise Ad.DoesNotExist

            serializer = AdSerializer(ad, data, partial=True)
            
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'MESSAGE' : 'SUCCESS'}, status = status.HTTP_200_OK)

            return Response({'MESSAGE' : 'KEY_ERROR'}, status = status.HTTP_400_BAD_REQUEST)

        except Ad.DoesNotExist:
            return Response({'MESSAGE':'AD_DOES_NOT_EXIST'}, status = status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        """
        정미정 (soft delete로 구현)
        """
        try:
            ad = Ad.objects.get(uid=uid)
            if ad.is_delete == True:
                raise Ad.DoesNotExist
            ad.delete_at = datetime.now()
            ad.is_delete = True
            ad.save()
            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=status.HTTP_200_OK)

        except Ad.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'AD_DOES_NOT_EXIST'}, status=status.HTTP_404_NOT_FOUND)

    else:
        return JsonResponse({'MESSAGE' : 'METHOD_NOT_ALLOWED'}, status = status.HTTP_405_METHOD_NOT_ALLOWED)
