from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,"Core/home.html")   

def about(request):
     return render(request,"Core/about-me.html")



def contact(request):
      return render(request,"Core/contact.html")

