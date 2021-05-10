from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import User
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed


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
        'data': 'Login to obtain API token'
    }

    return JsonResponse(response, status=status.HTTP_201_CREATED)
