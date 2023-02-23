from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def forums(request):
    return render(request,'forums.html')
    
def pro_ideas(request):
    return render(request,'pro_ideas.html')

def add(request):
    return render(request,'add.html')

def sal(request):
    return render(request,'sal.html')

def contact(request):
    return HttpResponse("This Is contact page")
