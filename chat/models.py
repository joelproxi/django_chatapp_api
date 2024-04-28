from django.db import models

from django.conf import settings
# Create your models here.


class Timestamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Conversation(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
    
    def __str__(self):
        return self.name
    
    
class Message(Timestamps):
    sender = models.ForeignKey(
                        to=settings.AUTH_USER_MODEL,
                        related_name='sender_user',
                        on_delete=models.CASCADE)
    receiver = models.ForeignKey(
                        to=settings.AUTH_USER_MODEL,
                        related_name='receiver_user',
                        on_delete=models.CASCADE
    )
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    is_edited = models.BooleanField(default=False)

    
class ChatGroup(Timestamps):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='owner_group',
        on_delete=models.CASCADE
    )
    members = models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='chatgroupuser')


class ChatgroupUser(Timestamps):
    group = models.ForeignKey(
        to=ChatGroup,
        on_delete=models.CASCADE,
        related_name='groups',
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='users_groups'
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    