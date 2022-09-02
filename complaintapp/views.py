from django.shortcuts import render
from complaintapp.forms import ComplaintCaptureForm
from complaintapp.models import (
    Complaints, 
    Locations,
    Tasks
)

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
    print(request.user)
    # List all open complaints
    ticket_qs = Complaints.objects.all()

    context = {
        'complaints': ticket_qs
    }

    return render(request, 'complaintapp/dashboard.html', context)