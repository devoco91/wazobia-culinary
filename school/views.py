from django.shortcuts import render,redirect
from .forms import  *
from django.contrib import messages
from .models import *
from django.db.models import Sum

# Create your views here.


def homepage(request):
    return render(request, 'school/index.html')

def aboutpage(request):
    return render(request, 'school/about.html')

def contactpage(request):
   
    
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
    else:
        form = ContactForm()
        
    context = {
    
        "form": form,  
    }
    
    return render(request, 'school/contact.html',context)

def dashboardpage(request):
    registrations = Registration.objects.all()  # Fetch all registrations
    contacts = ContactMessage.objects.all()  # Fetch all contact messages
    payments = Payment.objects.all()  # Fetch all Payment

    total_registrations = registrations.count()  # Get total registrations
    total_messages = contacts.count()  # Get total contact messages
    total_payments = payments.count()  # Get total payments
    total_amount_paid = Payment.objects.aggregate(Sum('amount_paid'))['amount_paid__sum'] or 0  # Default to 0 if no payments exist

    context = {
        "registrations": registrations,
        "contacts": contacts,
        "payments":payments,
        "total_registrations": total_registrations,
        "total_messages": total_messages,
        'total_payments': total_payments,
        'total_amount_paid': total_amount_paid
    }
    return render(request, 'school/dashboard.html', context)

def detailspage(request):
    return render(request, 'school/details.html')

def registerpage(request):
    
  
    
   
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        course = request.POST.get("course")
        mode_of_study = request.POST.get("mode_of_study")
        gender = request.POST.get("gender")
        shirt_size = request.POST.get("shirt_size")
        agree = request.POST.get("agree") == "on"

        # Save to database
        Registration.objects.create(
            name=name, email=email, address=address, phone=phone,
            course=course, mode_of_study=mode_of_study,
            gender=gender, shirt_size=shirt_size, agree=agree
        )

        return redirect("success")

  
    return render(request, 'school/register.html')


def successpage(request):
    return render(request, "school/success.html")
