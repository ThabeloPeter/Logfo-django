# views.py

from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from .models import CustomUser
from django.shortcuts import render
from .models import CustomUser

def user_list(request):
    # Query all instances of the CustomUser model
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})


def login_api(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # Login user
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def create_account_api(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        company_name = request.POST.get('company_name')

        # Check if email is already registered
        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already registered'}, status=400)

        # Create user account
        user = CustomUser.objects.create_user(email=email, password=password, company_name=company_name)
        if user is not None:
            return JsonResponse({'message': 'Account created successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Failed to create account'}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
