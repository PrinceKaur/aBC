# Registration
from task.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)
        

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SnippetList1(APIView):

    # serializer = RegisterSerializer(data=request.data)
    if User1=='seller':
        def post(self, request, format=None):
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
    if User1=='buyer':
        def get(self, request, format=None):
            snippets = User.objects.all()
            serializer = ProductSerializer(snippets, many=True)
            return Response(serializer.data)


# #Login 
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    
    if user:

        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(request, username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        print(token.key)
        return Response({'token': token.key},
                    status=HTTP_200_OK)
    
    if not user:
        return Response({'error': 'Invalid username and password'},
                        status=HTTP_404_NOT_FOUND)

        
#product add

class productlist(APIView):


    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = products.objects.all()
        serializer =ProductSerializer(snippets, many=True)
        return Response(serializer.data)
        

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

