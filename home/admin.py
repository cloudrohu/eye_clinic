from django.contrib import admin
from .models import *

class SettingAdmin(admin.ModelAdmin):
    list_display = ['id','title','website_link','color']
admin.site.register(Setting,SettingAdmin)

class Web_SliderAdmin(admin.ModelAdmin):
    list_display = ['id','web_image','mobile_image','title']
admin.site.register(Web_Slider,Web_SliderAdmin)

class OverviewAdmin(admin.ModelAdmin):
    list_display = ['id','web_image','title','details']
admin.site.register(Overview,OverviewAdmin)

class About_UsAdmin(admin.ModelAdmin):
    list_display = ['id','title','details']
admin.site.register(About_Us, About_UsAdmin)

class Unique_Selling_PropositionAdmin(admin.ModelAdmin):
    list_display = ['id','title','title2']
admin.site.register(Unique_Selling_Proposition,Unique_Selling_PropositionAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','icone','title']
admin.site.register(Service, ServiceAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id','web_image','title']
admin.site.register(Gallery, GalleryAdmin)

class BookingopenAdmin(admin.ModelAdmin):
    list_display = ['id','project_name','at','by','landp_arcel','floors','possession','spot_booking_offers','early_buy_discounts','flexipay_for_first','luxurious','priceing']
admin.site.register(Bookingopen, BookingopenAdmin)

class WelcometoAdmin(admin.ModelAdmin):
    list_display = ['id','title','details','readmore']
admin.site.register(Welcometo, WelcometoAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ['id','title']
admin.site.register(Location, LocationAdmin)


class AboutDoctorAdmin(admin.ModelAdmin):
    list_display = ['id','name','designation','qualification','experience','registration_no','contact_no','email']
admin.site.register(About_Doctor, AboutDoctorAdmin)


