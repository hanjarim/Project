from django.urls import path
from .views import (
    CustomerComplaint,
    Dashboard,
    ViewDetails,
    ListPendingTasks,
    AddTaskActions
)

app_name = 'complaintapp'

urlpatterns = [
    path('', CustomerComplaint, name='complaintform'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('details/<int:complaintid>/', ViewDetails, name='details'),
    path('tasks/', ListPendingTasks, name='pendingtasks'),
    path('actions/<int:taskid>/', AddTaskActions, name='actions'),
]