from django.urls import path
from .views import (
    CustomerComplaint,
)

app_name = 'complaintapp'

urlpatterns = [
    path('', CustomerComplaint, name='complaintform'),
]