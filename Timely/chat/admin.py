from chat.models import ChatMessage, CalendarEvent
from django.contrib import admin
# Register your models here.
@admin.register(CalendarEvent)
class ChatMessageAdmin(admin.ModelAdmin):
    pass


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    pass