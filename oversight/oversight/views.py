from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,HttpResponse
import openai

# Create your views here.

def chatbot_response(user_input):
    response = openai.Completion.create(
    engine="text-davinci-003",
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
    if request.method == 'POST':
        input_text = request.POST['input']
        response = chatbot_response("is "+input_text+"related to science answer in yes or no")
        response2 = chatbot_response("is "+input_text+"a form of greeting answer in yes or no")
        response = response.strip()
        response2 = response2.strip()
        if response == "Yes" or response2 == "Yes" or "college" in input_text or "engineering" in input_text or "engg" in input_text:
            response = chatbot_response(input_text)
        else:
            response = "Please enter engineering related queries"
        return JsonResponse({'response':response})
    else:
        return render(request,'forums.html')
    
def pro_ideas(request):
    degree = float(request.POST.get("degree",-1))
    type = float(request.POST.get("type",-1))
    domain = request.POST.get("domain",-1)
    
    if degree != -1 or type != -1 or domain != -1:
        if degree == 1:
            degree = "Bachelors"
        else:
            degree = "Masters"
        
        if type == 1:
            type = "Mini"
        else:
            type = "Major"
        
        response = chatbot_response("List projects in bullet points that can be made for a "+type+" project "+"in the domain of "+domain+" for a "+degree+" degree student with their online examples")
    else:
        response = ""
    
    return render(request,'pro_ideas.html',{'response' : response})

def notes(request):
    type = float(request.POST.get("type",-1))
    chp = request.POST.get("chp","")
    sub = request.POST.get("sub","")
    sem = request.POST.get("sem","")
    branch = request.POST.get("branch","")
    response = ""
    if type==1:
        response = chatbot_response("notes on "+chp+","+sub+" for sem"+sem+branch+"engineering")
    elif type==2:
        response = chatbot_response("generate 10 practice questions on "+chp+","+sub+" for sem"+sem+branch+"engineering")
    else:
        response = ""
    
    return render(request,'notes.html',{'response' : response})

def contact(request):
    return HttpResponse("This Is contact page")
