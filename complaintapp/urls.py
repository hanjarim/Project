from django.urls import path
from .views import (
    CustomerComplaint,
    Dashboard,
    ViewDetails,
    ListPendingTasks,
    AddTaskActions,
    TicketStatus,
    TicketView
)

app_name = 'complaintapp'

urlpatterns = [
    path('', CustomerComplaint, name='complaintform'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('details/<int:complaintid>/', ViewDetails, name='details'),
    path('tasks/', ListPendingTasks, name='pendingtasks'),
    path('actions/<int:taskid>/', AddTaskActions, name='actions'),
    path('charts/', TicketView, name='charts'),
    path('api/v1/tickets/', TicketStatus, name='ticketstatus'),
]