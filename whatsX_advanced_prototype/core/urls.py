from django.urls import path
from . import views

urlpatterns = [
    # Changed the root path to point to the new landing page
    # path('', views.landing_page, name='landing_page'),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('send-message/', views.send_message, name='send_message'),
    path('history/', views.message_history, name='message_history'),
]