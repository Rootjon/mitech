from django.shortcuts import render
from django.db.models import Count
from django.db.models import Q
from.forms import AppointmentForm,ContactForm,CommentForm,ContactusForm
from django.http import HttpResponseRedirect
from.models import Brand, Testimonial,Demo,Expert,Service,Award,Appointment,Design,Post,Album
from django.contrib import messages
from django.shortcuts import redirect
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

def contactt(request):
    
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

    return render(request,'app/home.html',context)

def itservice (request):
    designs=Design.objects.all()

    context={
        'designs':designs,


    }

    return render(request,'app/it-service.html',context)
def blog (request):
    posts=Post.objects.all()

    context={
        'posts':posts,


    }

    return render(request,'app/blog.html',context)


def blog_details (request, slug):
    post = Post.objects.get(slug=slug)
    comments = post.comments.filter(approve=True)
    
    if request.method == 'POST':
        
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            
            new_comment = comment_form.save(commit=False)
            
            new_comment.post = post
            
            new_comment.save()
            # redirect to a new URL:
            
            messages.success(request, 'Your comment submitted.')
            return HttpResponseRedirect(request.path_info)

    
    
    
    # if a GET (or any other method) we'll create a blank form
    else:
        
        comment_form = CommentForm()
    
    context={
        'post':post,
        'comments':comments,
        

    }

    return render (request,'app/details.html',context)

def about (request):
    testimonial=Testimonial.objects.all()
    brands=Brand.objects.all()
    albums=Album.objects.all()

    context={
        'testimonial':testimonial,
        'brands':brands,
        'albums':albums,
    }

    return render(request,'app/about.html',context)

def contact (request):
    
    
    if request.method == 'POST':
        
        contacts_form = ContactusForm(request.POST)
        
        
        if contacts_form.is_valid():
            
            contacts_form.save()
           
            # redirect to a new URL:
            return HttpResponseRedirect(request.path_info)
        
        
        
        
    
    
    # if a GET (or any other method) we'll create a blank form
    else:
        contacts_form = ContactusForm()


    context={
        
    }
    return render(request,'app/contact.html',context)

def search_blog(request):
    queryset1 = Testimonial.objects.all()
    queryset2 = Demo.objects.all()
    queryset3 = Expert.objects.all()
    queryset4 = Service.objects.all()
    queryset5 = Award.objects.all()
    queryset6 = Design.objects.all()
    queryset7 = Post.objects.all()
    queryset8 = Album.objects.all()
    brands=Brand.objects.all()
    
    
    query = request.GET.get('q')
    
    


    if query:
        queryset1=queryset1.filter(
            Q(title__icontains=query) | Q(designation__icontains=query) |
            Q(description__icontains=query)

        ).distinct()
        
        queryset2=queryset2.filter(
            Q(title__icontains=query) | Q(designation__icontains=query) |
            Q(description__icontains=query)

        ).distinct()
        
        queryset3=queryset3.filter(
            Q(title__icontains=query) | Q(designation__icontains=query) |
            Q(social_facebook__icontains=query) | Q(social_github__icontains=query)

        ).distinct()
        
       
        queryset4=queryset4.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)

        ).distinct()
        queryset5=queryset5.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)

        ).distinct()
        queryset6=queryset6.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)

        ).distinct()
        queryset7=queryset7.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)

        ).distinct()
        queryset8=queryset8.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)

        ).distinct()
       
    context = {
        "queryset1":queryset1,
        "queryset2":queryset2,
        "queryset3":queryset3,
        "queryset4":queryset4,
        "queryset5":queryset5,
        "queryset6":queryset6,
        "queryset7":queryset7,
        "queryset8":queryset8,
        'query':query,
        'brands':brands,
    }
    return render(request,'app/search.html', context)