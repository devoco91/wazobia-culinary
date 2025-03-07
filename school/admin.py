from django.contrib import admin
from .models import *

# Register your models here.



class RegistrationAdmin(admin.ModelAdmin):
    list_display=('name','email','address','phone', 'course', 'mode_of_study', 'shirt_size','date_registered')
    list_filter=('name','course','mode_of_study','shirt_size', 'date_registered')
    
class ContactMessageAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message', 'created_at')
    list_filter=('name','created_at')
    
class PaymentAdmin(admin.ModelAdmin):
    list_display=('student','course', 'amount_paid','date_paid' )
    list_filter=('student','course','amount_paid','date_paid')
    
   

admin.site.register(Registration, RegistrationAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Payment,  PaymentAdmin)

