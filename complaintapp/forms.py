from django import forms
from complaintapp.models import Complaints

class ComplaintCaptureForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ['phone', 'email','location','landmark', 'details', 'category']
        