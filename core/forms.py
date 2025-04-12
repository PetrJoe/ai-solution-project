from django import forms
from .models import ContactMessage, DemoRequest, EventRegistration

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'subject': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'message': forms.Textarea(attrs={'rows': 4, 'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }

class DemoRequestForm(forms.ModelForm):
    # Add these as non-model fields
    job_title = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    solution_of_interest = forms.ChoiceField(choices=[
        ('', 'Select a solution'),
        ('virtual_assistant', 'AI Virtual Assistant'),
        ('workflow_automation', 'Workflow Automation'),
        ('data_analytics', 'Data Analytics'),
        ('employee_engagement', 'Employee Engagement'),
        ('custom_solution', 'Custom Solution')
    ], widget=forms.Select(attrs={
        'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    consent = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={
        'class': 'mt-1 mr-2'
    }))
    
    class Meta:
        model = DemoRequest
        fields = ['name', 'email', 'company', 'phone', 'preferred_date', 'preferred_time', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'company': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'phone': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'preferred_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'preferred_time': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'message': forms.Textarea(attrs={'rows': 4, 'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['name', 'email', 'company', 'job_title']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Email Address'}),
            'company': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Company'}),
            'job_title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Job Title'}),
        }
