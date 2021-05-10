from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import User
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.auth.model import Token
from rest_framework.auth import login, authenticate





def register(request):
    email = request.data.get('email')
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        raise AuthenticationFailed('Username already exist!')

    User.objects.create(
        email=email,
        username=username,
        password=password
    )

    response = {
        'username': username,
        'status': status.HTTP_201_CREATED,
        'data': 'Login to obtain API token',
    }

    return JsonResponse(response, status=status.HTTP_201_CREATED)







def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = User.objects.filter(username=username)

    if not user.check_password(password):
        raise AuthenticationFailed('Wrong password!')
    
    auth_user = authenticate(username=username, password=password)
    if not auth_user in User.objects.all():
        raise AuthenticationFailed('User does not exist!')
    
    else:
        login(request, auth_user)
        token = str(Token.objects.create(user=auth_user))

        response = {
            'data': 'Successful login',
            'token': token,
            'status': status.HTTP_200_OK,
        }


    return JsonResponse(response, status=status.HTTP_200_OK)