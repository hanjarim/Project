from django.urls import path
from .views import (
    CustomerComplaint,
    Dashboard
)

app_name = 'complaintapp'

urlpatterns = [
    path('', CustomerComplaint, name='complaintform'),
    path('dashboard/', Dashboard, name='dashboard'),
]