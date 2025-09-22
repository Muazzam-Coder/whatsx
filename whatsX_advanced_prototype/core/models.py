from django.db import models
from django.contrib.auth.models import User

class MessageTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
# ... (existing MessageTemplate model)

class Contact(models.Model):
    phone_number = models.CharField(max_length=20, unique=True, help_text="Contact's phone number, e.g., +1234567890")
    name = models.CharField(max_length=100, blank=True, null=True)
    # You might add 'user' here if contacts belong to specific end-users
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name or 'Unknown'} ({self.phone_number})"
    

class MessageHistory(models.Model):
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    message_content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Sent')

    def __str__(self):
        return f"To {self.recipient_name} from {self.sent_by.username} at {self.sent_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name_plural = "Message History"
        ordering = ['-sent_at'] # Show the newest messages first