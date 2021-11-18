from django.contrib import admin
from.models import Testimonial,Demo,Expert,Service,Brand,Award
# Register your models here.

@admin.register(Testimonial)
class TestimonialModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','designation','image'
    ]

@admin.register(Demo)
class DemoModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','designation','image'
    ]


@admin.register(Expert)
class ExpertModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','designation','image','social_facebook',
    ]

@admin.register(Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','image',
    ]

@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    list_display=[
        'image',
    ]

@admin.register(Award)
class AwardModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','image',
    ]