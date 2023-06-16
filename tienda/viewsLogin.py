from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    email1 = data['email']
    contrasena1 = data['password']

    try:
        user = User.objects.get(email = email1)
    except User.DoesNotExist:
        return Response("Usuario invalido")
    
    pass_valida = check_password(contrasena1, user.password)
    if not pass_valida:
        return Response("Contraseña invalida")
    
    token,created = Token.objects.get_or_create(user=user)

    return Response(token.key)