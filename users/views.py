from rest_framework.views import APIView

from users.serializer import UserRegisterSerilizer , UserLoginSerilizer

from rest_framework.response import Response

from rest_framework import status

from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

class UserRegister(APIView):

    def post(self, request):

        serializer = UserRegisterSerilizer(data = request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({'message': 'successfully registered'},status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):

    authentication_classes = []

    permission_classes = []

    def post(self , request):

        serilizer = UserLoginSerilizer(data = request.data)

        if serilizer.is_valid():

            phone_number = serilizer.validated_data['phone_number']

            password = serilizer.validated_data['password']

            user_valid = authenticate(request , username = phone_number , password = password)

            if user_valid is not None:

                refrish = RefreshToken.for_user(user_valid)

                return Response({'message' : 'login was seccessful' , 'access' : str(refrish.access_token) , 'refrish' : str(refrish)} , status=status.HTTP_200_OK)

            return Response({'error' : 'password or phonenumber is invalid'} , status=status.HTTP_401_UNAUTHORIZED)

        return Response({'mess' : 'invalid request'} , status=status.HTTP_400_BAD_REQUEST)