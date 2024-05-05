from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


from .models import CustomUserModel
from .serializers import RegisterSerializer, MyTokenObtainClaimSerializer


class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainClaimSerializer


class RegisterUser(CreateAPIView):
    permission_classes = [AllowAny,]
    queryset = CustomUserModel.objects.all()
    serializer_class = RegisterSerializer

    # def post(self, request):
    #     serializer = RegisterSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class UserModelViewset(ModelViewSet):
    queryset = CustomUserModel.objects.all()
    serializer_class = RegisterSerializer
