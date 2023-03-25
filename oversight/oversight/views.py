from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
import openai

# Create your views here.

def chatbot_response(user_input):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=user_input,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    return response["choices"][0]["text"]

def index(request):
    return render(request,'index.html')
    
def forums(request):
    return render(request,'forums.html')
    
def pro_ideas(request):
    user_input = ""
    user_input = request.POST.get("user_input")
    if user_input != None:
        response = chatbot_response(user_input)
    else:
        response = ""
    
    return render(request,'pro_ideas.html',{'response' : response})

def add(request):
    return render(request,'add.html')

def contact(request):
    return HttpResponse("This Is contact page")
