from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import ConversationViewset


router = DefaultRouter()
router.register('conversations', ConversationViewset, basename='conversations')

urlpatterns = [
    
] + router.urls
