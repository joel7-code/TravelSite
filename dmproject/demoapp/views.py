from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from . models import Place

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})

#def about(request):
    #return HttpResponse("About Page")

#def contact(request):
    #return render(request,"contact.html")

#def detail(request):
    #return HttpResponse("Details Page")

#def thanks(request):
    #return render(request,"thanks.html")

