from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.user_serializer import UserSerializer,UserRegisterSerializer
from ..models.user_model import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegistrationView(APIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        uid = response['user_id']
        token = response['token']
        return Response({"message": "Usuario creado con éxito", "uid": uid, "token": token}, status=status.HTTP_201_CREATED)

# class UserRegistrationView(APIView):
#     def post(self, request):
#         serializer = UserRegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Usuario creado con éxito"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
