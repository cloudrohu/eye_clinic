from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.http import request
from django.utils.safestring import mark_safe




# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=150,)
    website_link = models.CharField(max_length=150,)
    keywords = models.CharField(max_length=255,)
    description = models.CharField(max_length=255,)
    configuration_bg = models.ImageField(upload_to='logo/')
    logo = models.ImageField(upload_to='logo/',)
    icon = models.ImageField(upload_to='images/',)
    virtual_site_visit = models.ImageField(upload_to='images/',)
    color = models.CharField(max_length=150)
    cuntact_no = models.CharField(max_length=150,)
    location = models.CharField(max_length=1150,)
    site_address= models.CharField(max_length=1150,blank=True,null=True)
    googletagmanager= models.CharField(max_length=1150,blank=True,null=True)
    privacy_policy = RichTextField(blank=True,null=True)
    
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='9. Header'

class Web_Slider(models.Model):
    web_image = models.ImageField(upload_to='sliderimage/')
    mobile_image = models.ImageField(upload_to='sliderimage/')
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='2. Web Slider'

class Overview(models.Model):
    web_image = models.ImageField(upload_to='overviewimage/')
    title = models.CharField(max_length=150)
    details= models.TextField(blank=False,max_length=5500)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='3. Overview'

class About_Us(models.Model):
    title = models.CharField(max_length=150)
    details= models.TextField(blank=False,max_length=5500)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='4. About_Us'

class Unique_Selling_Proposition(models.Model):
    title = models.CharField(max_length=150)
    title2 = models.CharField(max_length=150,blank=True,null=True)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='5. Unique Selling Proposition'

class Service(models.Model):
    icone = models.ImageField(upload_to='amenitiesimage/')
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='7. Amenities'

class Gallery(models.Model):   
    web_image = models.ImageField(upload_to='galleryimage/')
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='8. Gallery'
     

class Bookingopen(models.Model):
    project_name = models.CharField(max_length=150,)
    at = models.CharField(max_length=255,)
    by = models.CharField(max_length=255,)
    landp_arcel = models.CharField(max_length=255,)
    floors = models.CharField(max_length=255,)
    possession = models.CharField(max_length=255,)
    spot_booking_offers = models.CharField(max_length=255,)
    early_buy_discounts = models.CharField(max_length=255,)
    flexipay_for_first = models.CharField(max_length=255,)
    luxurious = models.CharField(max_length=255,)
    priceing = models.CharField(max_length=255,)
 
    
    def __str__(self):
        return self.project_name    
        
    class Meta:
        verbose_name_plural='10. Booking Open'

class Welcometo(models.Model):
    web_image = models.ImageField(upload_to='aboutimage/')
    title = models.CharField(max_length=150)
    details= models.TextField(blank=False,max_length=5500)
    readmore= models.TextField(blank=False,max_length=5500)
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='11. Welcome To'

class Location(models.Model):
    title = models.CharField(max_length=150)    
    
    def __str__(self):
        return self.title    
        
    class Meta:
        verbose_name_plural='12. Location'



class About_Doctor(models.Model):
    name = models.CharField(max_length=200)                # Doctor ka naam
    designation = models.CharField(max_length=200)         # e.g., Eye Surgeon, Cardiologist
    qualification = models.CharField(max_length=300)       # e.g., MBBS, MS, Fellowship etc.
    experience = models.PositiveIntegerField()             # e.g., 16 (years)
    specialization = models.TextField()                    # e.g., Cataract, Glaucoma, Oculoplasty
    description = models.TextField()                       # Doctor ka about paragraph
    photo = models.ImageField(upload_to="doctor_photos/")  # Profile photo
    registration_no = models.CharField(max_length=100, blank=True, null=True) # e.g., MCI Reg. No
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    clinic_address = models.TextField(blank=True, null=True)
    timings = models.CharField(max_length=200, blank=True, null=True)  # e.g., Mon-Sat: 9AM–2PM
    social_links = models.URLField(blank=True, null=True)  # e.g., LinkedIn/Website link

    class Meta:
        verbose_name = "Doctor Profile"
        verbose_name_plural = "Doctor Profiles"

    def __str__(self):
        return self.name




