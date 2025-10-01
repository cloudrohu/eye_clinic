from django.contrib import admin
from django.utils.html import format_html
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
admin.site.register(Media, GalleryAdmin)

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

class StatAdmin(admin.ModelAdmin):
    list_display =  ['title', 'total',]


class FAQsAdmin(admin.ModelAdmin):
    list_display =  ['Question', 'Answer']
    
class Why_ChooseAdmin(admin.ModelAdmin):
    list_display =  ['title', 'description']
    
class HealthTipAdmin(admin.ModelAdmin):
    list_display =  ['title', 'short_description']


@admin.register(ClientReview)
class ClientReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "rating", "is_active", "order", "created_at", "photo_preview")
    list_editable = ("is_active", "order", "rating")
    search_fields = ("name", "city", "review_text")
    list_filter = ("is_active", "rating")
    readonly_fields = ("created_at", "photo_preview")
    prepopulated_fields = {"slug": ("name",)}

    fieldsets = (
        (None, {
            "fields": (
                "name", "city", "slug", "photo", "photo_preview", 
                "rating", "review_text", "order", "is_active"
            )
        }),
        ("Timestamps", {
            "fields": ("created_at",),
            "classes": ("collapse",),
        }),
    )

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height:80px; border-radius:50%;" />', obj.photo.url)
        return "(No photo)"
    photo_preview.short_description = "Photo"

class TPAAdmin(admin.ModelAdmin):
    list_display =  ['title', 'details']
    

admin.site.register(Stat,StatAdmin)
admin.site.register(FAQs,FAQsAdmin)
admin.site.register(Why_Choose,Why_ChooseAdmin)
admin.site.register(TPA,TPAAdmin)
admin.site.register(HealthTip,HealthTipAdmin)


