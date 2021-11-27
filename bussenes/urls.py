from django.urls import path
from . import views

app_name='bussenes'

urlpatterns = [
    path('',views.home,name='home'),
    path('contactt/', views.contactt, name='contactt'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search_blog, name='search'),
    path('it_service/', views.itservice, name='it_service'),
    path('aboutus_us/', views.about, name='about'),
    path('contact_us/', views.contact, name='contact_us'),
    path('blog/', views.blog, name='blog_post'),
    path('blog/<slug>/', views.blog_details, name='details'),
]
