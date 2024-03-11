# users/urls.py

from django.urls import path
from users import views
from django.contrib import admin


urlpatterns = [
    path('api/login/', views.login_api, name='login_api'),
    path('api/create_account/', views.create_account_api, name='create_account_api'),
    path('admin/', admin.site.urls),
    # Add more API endpoints as needed
]
