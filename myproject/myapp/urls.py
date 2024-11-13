# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # The home view will be shown at the root URL
    # path('execute/', views.execute_python_code, name='execute_python_code'),
]