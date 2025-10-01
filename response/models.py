from django.db import models

# Create your models here.


class Response(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=100, blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)  # sets once when created
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Response'
        ordering = ['-created_at']
        # ordering = ['-id']    



class Appointment(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    appointment_date = models.DateTimeField(verbose_name="Appointment Date & Time")
    message = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.name} on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Appointment Request"
        verbose_name_plural = "Appointment Requests"
        ordering = ['appointment_date']        