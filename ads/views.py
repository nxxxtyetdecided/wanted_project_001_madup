from django.shortcuts import render
from rest_framework.decorators import api_view


@api_view(['PATCH', 'DELETE'])
def update_delete_ad(request):
    if request.method == 'PATCH':
        pass


    elif request.method == 'DELETE':
        pass