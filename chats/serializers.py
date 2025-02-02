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
        extra_kwargs = {
            'slug': {
                'read_only': True
            }
        }
        

class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = [
            'id',
            'sender',
            'receiver',
            'text_content',
            'is_read',
            'is_edited',
        ]