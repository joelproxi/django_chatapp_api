from rest_framework import serializers

from .models import Message, ChatGroup, ChatgroupUser, Conversation


class ConversationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Conversation
        fields = [
            'id',
            'name',
            'slug',
        ]
        

# class MessageSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Message
#         fields = [
#             'id',
#         ]