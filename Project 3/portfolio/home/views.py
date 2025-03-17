from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse('hey')
    return render(request, 'index.html')

def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')

def contact(request):
    # Handle the form here
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        email = request.POST['email']
        print(email)
        phone = request.POST['phone']
        print(phone)
        desc = request.POST['desc']
        print(desc)
        c = Contact(name = name, email = email, phone = phone, desc = desc)
        c.save()
        
    return render(request, 'contact.html')