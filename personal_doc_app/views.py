from django.shortcuts import render

# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework import status

# from personal_doc_app.models import Users
# from personal_doc_app.serializers import UsersSerializers
# from rest_framework.decorators import api_view

# from mongo_auth

# Create your views here.


# @api_view(['POST'])
# def login(request):
#   # login user
#   try: 
#         tutorial = mongo_auth 
#     except Tutorial.DoesNotExist: 
#         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 


# @api_view(['POST'])
# def register(request):
#   # login user

from datetime import datetime
from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Personal Doc Api!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
