from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm
from .models import Alert
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'loginapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home page after successful login
        else:
            return render(request, 'loginapp/login.html', {'error': 'Invalid credentials'})  # Show error for invalid login
    
    return render(request, 'loginapp/login.html')

@login_required
def home_view(request):
    return render(request, 'loginapp/home.html')

def default_view(request):
    if request.user.is_authenticated:
        return redirect('home')  
    else:
        return redirect('login')
def temparatures_view(request):
    return render(request, 'loginapp/temparatures.html')
def cycloneprediction_view(request):
    return render(request, 'loginapp/cyclone_prediction.html')

@login_required
def recent_alerts_view(request):
    alerts = Alert.objects.all().order_by('-id') 
    return render(request, 'loginapp/recent_alerts.html', {'alerts': alerts})

@login_required
def add_alert_view(request):
    if request.user.is_superuser:  # Ensure only superusers can access this view
        if request.method == 'POST':
            region = request.POST.get('region')
            alert_type = request.POST.get('alert_type')
            description = request.POST.get('description')
            date = request.POST.get('date')
            Alert.objects.create(region=region, alert_type=alert_type, description=description, date=date)
            return redirect('recent_alerts')
        return render(request, 'loginapp/add_alert.html')
    else:
        return redirect('recent_alerts')

@login_required
def delete_alert_view(request, alert_id):
    if request.method == "POST":
        alert = get_object_or_404(Alert, id=alert_id)
        alert.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def edit_alert_view(request, alert_id):
    alert = get_object_or_404(Alert, id=alert_id)
    if request.method == "POST":
        alert.region = request.POST.get('region')
        alert.alert_type = request.POST.get('alert_type')
        alert.description = request.POST.get('description')
        alert.date = request.POST.get('date')
        alert.save()
        return redirect('recent_alerts')  # Redirect to recent alerts after updating
    return render(request, 'loginapp/edit_alert.html', {'alert': alert})
