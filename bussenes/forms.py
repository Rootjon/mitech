from django import forms
from .models import Appointment,Contact,Comment,Contactus

class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ('name', 'email', 'department' )

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'department','message' )
        
class CommentForm(forms.ModelForm):
    
    class Meta:

        model = Comment
        fields = ('name','body','email')
        
class ContactusForm(forms.ModelForm):
        
    class Meta:
        model = Contactus
        fields = ('name', 'email', 'subject','message' )