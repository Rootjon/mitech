from django.shortcuts import render
from.models import Brand, Testimonial,Demo,Expert,Service,Award
# Create your views here.

def home (request):
    testimonial=Testimonial.objects.all()
    demos=Demo.objects.all()
    experts=Expert.objects.all()
    services=Service.objects.all()
    brands=Brand.objects.all()
    awards=Award.objects.all()
  

    context={
      'testimonial':testimonial, 
      'demos':demos,
      'experts':experts,
      'services':services,
      'brands':brands,
      'awards':awards,
      
    }
    return render(request,'app/home.html',context)