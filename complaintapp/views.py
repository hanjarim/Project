from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import render, redirect
from complaintapp.forms import (
    ComplaintCaptureForm, 
    ComplaintViewForm,
    CreateTaskForm
) 
from complaintapp.models import (
    Complaints, 
    Locations,
    Tasks
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
    ticket_qs = Complaints.objects.all()

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
            print("COMPLAINT", complaint_obj)

            obj, create = Tasks.objects.get_or_create(
                complaint=complaint_obj,
                defaults={'user':engineer_obj, 'status':'PENDING'}
            )

            if create:
                text = "Task successfully assigned"
                messages.success(request, text)
                return redirect('complaintapp:details')
            if not create:
                text = "Task already assigned"
                messages.success(request, text)
                return redirect('complaintapp:details')


    except Exception as e:
        print(f"Error occured: {str(e)}")

    return render(request, 'complaintapp/details.html', context)


def CreateTask(request):
    if request.method == 'POST':
        taskform = CreateTaskForm(request.POST)

        if form.is_valid():
            # Add a new task
            pass
    return render(request, 'complaintapp/tasks.html', context)