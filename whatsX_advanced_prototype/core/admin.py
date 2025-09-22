from django.contrib import admin
from .models import MessageTemplate, Contact, MessageHistory

@admin.register(MessageTemplate)
class MessageTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at', 'updated_at')
    search_fields = ('name', 'content')
    list_filter = ('created_by', 'created_at')

    def save_model(self, request, obj, form, change):
        if not obj.pk: # Only set created_by on creation
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
# ... (existing MessageTemplateAdmin)
from .models import MessageTemplate, Contact


@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('recipient_name', 'phone_number', 'sent_by', 'sent_at', 'status')
    list_filter = ('sent_at', 'sent_by', 'status')
    search_fields = ('recipient_name', 'phone_number', 'message_content')
