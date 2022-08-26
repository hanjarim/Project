from django.shortcuts import render
from complaintapp.forms import ComplaintCaptureForm

def CustomerComplaint(request):
    form = ComplaintCaptureForm(request.POST or None)
    context = {
        'form': form
    }

    return render(request, 'complaintapp/complaint.html', context)