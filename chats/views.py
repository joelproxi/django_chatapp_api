from django.shortcuts import render

from rest_framework import viewsets

from .models import Conversation
from .serializers import ConversationSerializer
# Create your views here.

class ConversationViewset(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    
    
