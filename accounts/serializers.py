from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUserModel


class MyTokenObtainClaimSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: CustomUserModel) -> Token:
        token = super().get_token(user)
        token["email"] = user.email
        token["phone"] = user.phone

        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUserModel
        fields = (
            "id",
            "full_name",
            "phone",
            "email",
            "password",
            "password2"
        )

        extra_fields = {
            "id": {
                "read_only": True,
            },
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {_("password"): _("Password fields didn't match.")})
        return attrs

    def create(self, validated_data):
        email = validated_data.get("email")
        phone = validated_data.get("phone")
        full_name = validated_data.get("full_name")
        password = validated_data['password']
        user = CustomUserModel.objects.create(
            email=email,
            phone=phone,
            full_name=full_name
        )
        user.set_password(password)
        user.save()
        return user
