# Generated by Django 5.0.4 on 2024-04-28 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_coversation_conversation_message_is_edited_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='text_content',
        ),
    ]