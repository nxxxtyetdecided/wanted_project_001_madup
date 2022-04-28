from django.shortcuts import render
from rest_framework.decorators import api_view

@api_view(['POST'])
def get_create_ad(request):
    if request.method == 'GET':
        pass    


@api_view(['PATCH', 'DELETE'])
def update_delete_ad(request):
    if request.method == 'PATCH':
        pass


    elif request.method == 'DELETE':
        pass
