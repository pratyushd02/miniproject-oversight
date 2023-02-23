from django.shortcuts import render
import joblib
import csv
# Create your views here.

def predict(request):
    output = 99
    model = joblib.load('salarypredmodel.sav')
    gender = request.POST.get("gender",-1)
    if gender=="Male":
        gender=0
    else:
        gender=1
    
    uni = float(request.POST.get("uni",-1))
    degree = float(request.POST.get("degree",-1))
    sp = float(request.POST.get("specialization",-1))
    pt = float(request.POST.get("cgpa",-1)) * 10
    yr = int(request.POST.get("year",-1))
    
    if(gender == -1 or uni == -1 or degree == -1 or sp == -1 or pt == -10 or yr == -1 ):
        return render(request, 'form_salary.html',{'output' : output})
    else:
        
          
        output = round(model.predict([[gender,uni,degree,sp,pt,yr]])[0]) 
    
    return render(request, 'form_salary.html',{'output' : output })