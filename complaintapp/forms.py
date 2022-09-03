from django import forms
from complaintapp.models import Complaints, Tasks

class ComplaintCaptureForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ['phone', 'email','location','landmark', 'coordinates', 'details', 'category']

        labels = {
            'phone': 'Phone number',
            'email': 'Email',
            'location': 'Location',
            'landmark': 'Landmark',
            'coordinates': 'Coordinates',
            'category': 'Category',
            'details': 'Details',
            
        }

        help_texts = {
            'phone': 'Please provide a contact to reach you back with',
            'email': 'Email address to reach you',
            'location': 'Location',
            'landmark': 'A physical feature nearest to where you experience the problem.',
            'coordinates': 'S035 E45',
            'details': 'Details',
            'category': 'Is it a data or call problem?'
        }

        widgets = {
            'phone': forms.TextInput(attrs={
                'placeholder':'Phone number',
                'class': 'input'
            }),
            'email': forms.TextInput(attrs={
                'placeholder':'Email address',
                'class': 'input'
            }),
            'location': forms.Select(attrs={
                'class': 'custom_select'
            }),
            'landmark': forms.TextInput(attrs={
                'placeholder':'Land mark',
                'class': 'input'
            }),
            'coordinates': forms.TextInput(attrs={
                'placeholder':'S035 E45',
                'class': 'input'
            }),
            'category': forms.Select(attrs={
                'class': 'custom_select'
            }),
            'details': forms.Textarea(attrs={
                'cols':80, 'rows':20,
                'placeholder': 'Describe the problem currently being experienced',
                'class': 'textarea'
            }),
        }

class ComplaintViewForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ['phone', 'email','location','landmark', 'coordinates', 'details', 'category']
        read_only = ['date']
        labels = {
            'phone': 'Phone number',
            'email': 'Email',
            'location': 'Location',
            'landmark': 'Landmark',
            'coordinates': 'Coordinates',
            'category': 'Category',
            'details': 'Details'
        }

        widgets = {
            'phone': forms.TextInput(attrs={
                'placeholder':'Phone number',
                'disabled': 'readonly'
            }),
            'email': forms.TextInput(attrs={
                'placeholder':'Email address',
                'disabled': 'readonly'
            }),
            'location': forms.Select(attrs={
                'disabled': 'readonly'
            }),
            'landmark': forms.TextInput(attrs={
                'placeholder':'Land mark',
                'disabled': 'readonly'
            }),
            'coordinates': forms.TextInput(attrs={
                'placeholder':'S035 E45',
                'disabled': 'readonly'
            }),
            'category': forms.Select(attrs={
                'disabled': 'readonly'
            }),
            'details': forms.Textarea(attrs={
                'cols':40, 'rows':15,
                'placeholder': 'Describe the problem currently being experienced',
                'class': 'textarea',
                'disabled': 'readonly'
            }),
        }

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['complaint']