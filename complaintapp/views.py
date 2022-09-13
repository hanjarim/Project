from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from complaintapp.forms import (
    ComplaintCaptureForm, 
    ComplaintViewForm,
    CreateActionForm
) 
from complaintapp.models import (
    Complaints, 
    Locations,
    Tasks,
    TaskActions
)

User = get_user_model()

def CustomerComplaint(request):
    form = ComplaintCaptureForm(request.POST or None)

    if request.method == 'POST':
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        location = request.POST.get('location')
        landmark = request.POST.get('landmark')
        coordinates = request.POST.get('coordinates')
        category = request.POST.get('category')
        details = request.POST.get('details')

        # Get location
        location_qs = Locations.objects.get(pk=location)

        # Add a new record
        Complaints.objects.create(
            phone=phone,
            email=email,
            location=location_qs,
            landmark=landmark,
            category=category,
            details=details,
            coordinates=coordinates,
            status='open'
        )


    context = {
        'form': form
    }

    return render(request, 'complaintapp/complaint.html', context)

def Dashboard(request):

    # List all open complaints
    ticket_qs = Complaints.objects.filter(status__icontains='open')

    context = {
        'complaints': ticket_qs
    }

    return render(request, 'complaintapp/dashboard.html', context)

def ViewDetails(request, complaintid):
    try:
        complaint_qs = Complaints.objects.get(id=complaintid)
     
        info = {
            'id': complaint_qs.pk,
            'category': complaint_qs.category,
            'phone': complaint_qs.phone,
            'email': complaint_qs.email,
            'location': complaint_qs.location,
            'landmark': complaint_qs.landmark,
            'coordinates': complaint_qs.coordinates,
            'details': complaint_qs.details,
            'date': complaint_qs.date
        }

        details_form = ComplaintViewForm(initial=info)
        context = {
            'details': details_form,
            'complaintid': complaint_qs.pk
        }
        if request.method == 'POST':
            
            # Add a new task
            engineer_obj = User.objects.get(username=request.user)
            complaint_obj = Complaints.objects.get(pk=request.POST['complaint'])
            
            obj, create = Tasks.objects.get_or_create(
                complaint=complaint_obj,
                defaults={'user':engineer_obj, 'status':'PENDING'}
            )

            if create:
                text = "Task successfully assigned"
                messages.success(request, text)
               
            if not create:
                text = "Task already assigned"
                messages.success(request, text)

    except Exception as e:
        print(f"Error occured: {str(e)}")

    return render(request, 'complaintapp/details.html', context)

def ListPendingTasks(request):
    pending_tasks_qs = Tasks.objects.filter(user=request.user.id,status='PENDING')

    context = {
        'pending_tasks': pending_tasks_qs
    }

    return render(request, 'complaintapp/tasklist.html', context)

def AddTaskActions(request, taskid):
    
    task_qs = Tasks.objects.get(id=taskid)

    info = {
        'task': task_qs.id,
    }

    form = CreateActionForm(initial=info)
    if request.method == "POST":
        form = CreateActionForm(request.POST or None)
       
        # Add action 
        if form.is_valid():
            print("VALID", request.POST)

            # Check if close ticket is selected

            if request.POST['CloseTicket'] in request.POST:
                print("CLOSE THE TICKET")
                # Get the current task, update the status to CLOSED
                task_qs.status = "CLOSED"
                task_qs.save()

            
            form.save()
        else:
            print(form.errors)
    
    # List previous actions
    actions_qs = TaskActions.objects.filter(task=task_qs.id)



    context = {
        'actionform': form,
        'previousactions': actions_qs
    }

    return render(request, 'complaintapp/taskactions.html', context)


def TicketStatus(request):
    # Get count for the open, closed and pending tickets
    # return a JSON object that will be used to render a chart
    open_tickets = Complaints.objects.filter(status__icontains='OPEN').count()
    closed_tickets = Complaints.objects.filter(status__icontains='CLOSED').count()
    pending_tickets = Complaints.objects.filter(status__icontains='PENDING').count()

    data = {
        'OPEN': open_tickets,
        'CLOSED': closed_tickets,
        'PENDING': pending_tickets
    }

    return JsonResponse(data)


def TicketView(request):
    complaints_qs = Complaints.objects.latest('date')
    timestamp = complaints_qs.date.strftime("%b-%d-%Y %H:%M:%S")
    context = {
        'timestamp': timestamp
    }

    return render(request, 'complaintapp/charts.html', context)