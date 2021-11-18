from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from.forms import AppointmentForm,ContactForm
from django.http import HttpResponseRedirect
from.models import Brand, Testimonial,Demo,Expert,Service,Award,Appointment
# Create your views here.

def home (request):
    testimonial=Testimonial.objects.all()
    demos=Demo.objects.all()
    experts=Expert.objects.all()
    services=Service.objects.all()
    brands=Brand.objects.all()
    awards=Award.objects.all()

    if request.method == 'POST':
        
        appoint_form = AppointmentForm(request.POST)
        
        
        if appoint_form.is_valid():
            
            appoint_form.save()
           
            # redirect to a new URL:
            return HttpResponseRedirect(request.path_info)
        
        
        
        
    
    
    # if a GET (or any other method) we'll create a blank form
    else:
        appoint_form = AppointmentForm()
        
  

    context={
      'testimonial':testimonial, 
      'demos':demos,
      'experts':experts,
      'services':services,
      'brands':brands,
      'awards':awards,
      
    }
    return render(request,'app/home.html',context)

def contact(request):
    
    if request.method == 'POST':
        
        contact_form = ContactForm(request.POST)
        
        
        if contact_form.is_valid():
            
            contact_form.save()
           
            # redirect to a new URL:
            return HttpResponseRedirect('/')
        
        
        
        
    
    
    # if a GET (or any other method) we'll create a blank form
    else:
        contact_form = ContactForm()
        
    
    context = {

    }

    return render(request, 'nimuit/nimuit.html', context)