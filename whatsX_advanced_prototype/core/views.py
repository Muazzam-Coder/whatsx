from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MessageTemplate
from .models import MessageTemplate, MessageHistory
from .forms import SignUpForm
from django.contrib.auth import login  
# View for the public landing page
def landing_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'landing.html')

# View for the main dashboard after login
@login_required
def dashboard(request):
    # Calculate totals for the logged-in user
    total_messages_sent = MessageHistory.objects.filter(sent_by=request.user).count()
    # contacts_saved = Contact.objects.filter(owner=request.user).count() # Future goal
    
    context = {
        'total_messages_sent': total_messages_sent,
        'contacts_saved': 0, # Placeholder for now
    }
    return render(request, 'dashboard.html', context)
# View for the "Send Message" page
@login_required
def send_message(request):
    if request.method == 'POST':
        # This is where you would handle the form submission
        # For the prototype, we just print the data and redirect
        recipient_name = request.POST.get('recipient_name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        
        print(f"--- Message to Send ---")
        print(f"To: {recipient_name} ({phone_number})")
        print(f"Message: {message}")
        print(f"-----------------------")
        
        # Redirect back to the dashboard after "sending"
        return redirect('dashboard')
        
    return render(request, 'send_message.html')
@login_required
def send_message(request):
    # 1. Fetch all templates from the database
    templates = MessageTemplate.objects.all().order_by('name')

    if request.method == 'POST':
        # This is where you would handle the form submission
        recipient_name = request.POST.get('recipient_name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        
        print(f"--- Message to Send ---")
        print(f"To: {recipient_name} ({phone_number})")
        print(f"Message: {message}")
        print(f"-----------------------")
        
        return redirect('dashboard')
    
    # 2. Add the templates to the context dictionary
    context = {
        'templates': templates
    }
        
    return render(request, 'send_message.html', context)

@login_required
def send_message(request):
    templates = MessageTemplate.objects.all().order_by('name')

    if request.method == 'POST':
        recipient_name = request.POST.get('recipient_name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        
        # --- Create and save the history record ---
        MessageHistory.objects.create(
            sent_by=request.user, # The currently logged-in user
            recipient_name=recipient_name,
            phone_number=phone_number,
            message_content=message
        )
        
        return redirect('dashboard')
    
    context = {'templates': templates}
    return render(request, 'send_message.html', context)

@login_required
def message_history(request):
    # Fetch history for the currently logged-in user only
    history = MessageHistory.objects.filter(sent_by=request.user)
    context = {
        'history': history
    }
    return render(request, 'message_history.html', context)




def register(request):
    # If a user is already logged in, redirect them to the dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create the new user
            login(request, user)  # Log the new user in automatically
            return redirect('dashboard')  # Redirect to the main dashboard
    else:
        form = SignUpForm()
        
    return render(request, 'registration/register.html', {'form': form})