from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

router = DefaultRouter()

# router.register('users', views.UserModelSerializer, basename="users")

urlpatterns = [
    # Authentication
    path('login/', views.LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', views.RegisterUser.as_view(), name='registration'),

]
