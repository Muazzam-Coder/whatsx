# core/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# This is your existing form. Keep it as is.
class MessageForm(forms.Form):
    message_content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}), required=True)
    # Add other fields here if needed, e.g., 'recipients' for future integration


# --- ADD THIS NEW CLASS TO THE SAME FILE ---
class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',) # You can also add 'email' if you wish