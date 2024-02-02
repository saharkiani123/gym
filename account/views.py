from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from account.serializers import *
from account.models import *


class RegisterView(APIView):
    '''
        Signup users with username & password and check fields with serializers.
    '''
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"statuscode":200,"status":"success", "message":'کاربر با موفقیت ایجاد شد.'})
        else:
            print(serializer.errors)
            return Response({"status":402, "data":serializer.errors})
        

class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        
        user_info = {

            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'social_media_profiles': user.social_media_profiles,
            'email': user.email,
            'address': user.address
        }

        response_data = {
            "statuscode": 200,
            "status": "success",
            'user_info': user_info,
            "token": {
                'access_token': access_token,
                'refresh_token':f'{refresh}'
                 
            }
        }
        return Response(response_data)
    

