from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q, F
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.db import models
from django.shortcuts import redirect, render
from django.core.mail import send_mail
# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import translation
from django.views.decorators.http import require_POST
from django.contrib import messages
from response.models import Appointment
from datetime import datetime
from home.models import *
from response.models import Response
from django.utils.decorators import method_decorator


def index(request):
    header = Setting.objects.all().order_by('-id')[0:1]  
    slider = Web_Slider.objects.all().order_by('?')[0:6]  
    overview = Overview.objects.all().order_by('-id')[0:1]  
    about_us = About_Us.objects.all().order_by('-id')[0:1]  
    welcome = Welcometo.objects.all().order_by('-id')[0:1]  
    location = Location.objects.all().order_by('-id')     
    bookingopen = Bookingopen.objects.all().order_by('-id')[0:1]  
    doctor = About_Doctor.objects.all().order_by('-id')[0:1]  
    unique_Selling_Proposition = Unique_Selling_Proposition.objects.all()[0:3] 
    amenities = Service.objects.all()
    gallery = Gallery.objects.all().order_by('-id')
    service = Service.objects.all().order_by('-id')[0:4] 
    stat = Stat.objects.all().order_by('-id')[0:4] 



    context={
        'doctor':doctor,
        'location':location,
        'bookingopen':bookingopen,
        'welcome':welcome,
        'header':header,
        'slider':slider,
        'overview':overview,
        'about_us':about_us,
        'unique_Selling_Proposition':unique_Selling_Proposition,
        'amenities':amenities,
        'gallery':gallery,
        'service':service,
        'stat':stat,


    }
    return render(request,'index.html',context)



def privacy_policy(request): 
    header = Setting.objects.all().order_by('-id')[0:1]  

    context={
        'header':header,
    }
    return render(request,'privacy_policy.html',context)



def thank_you(request):
    return render(request, 'thank_you.html')


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('mobile')
 

         # Save to DB
        Response.objects.create(name=name, email=email, phone=phone)

        # Send "Thank You" email to user
        subject = 'Thank You for Contacting '
        message = f"""
Dear {name},

Thank you for Connecting. We have received your details:

Email: {email}  
Phone: {phone}

Our team will contact you shortly.

Kind regards 
All the best
"""
        from_email = None  # Uses DEFAULT_FROM_EMAIL in settings.py
        recipient_list = [email]  # ← Send to user, not to admin

        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            print("Error sending email:", e)
        return redirect('thank_you')  # Make sure this name matches urls.py

    return render(request, 'base.html')


@require_POST
def submit_appointment(request):
  
    try:
        # Get data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_str = request.POST.get('date')
        message = request.POST.get('message', '')

        # Convert the datetime-local string to a proper Python datetime object
        # Example format: 2024-10-25T14:30
        appointment_datetime = datetime.fromisoformat(date_str)

        # Create and save the new Appointment object
        Appointment.objects.create(
            name=name,
            email=email,
            phone=phone,
            appointment_date=appointment_datetime,
            message=message
        )
        
        # Display success message (requires Django's messages framework)
        messages.success(request, "thank-you.html")

    except Exception as e:
        # Display error message
        print(f"Error saving appointment: {e}")
        messages.error(request, "There was an error submitting your request. Please try again.")

    # Redirect the user back to the page they came from (or a success page)
    # Note: You might need to adjust the redirect URL based on your site structure
    return redirect(request.META.get('HTTP_REFERER', '/'))
