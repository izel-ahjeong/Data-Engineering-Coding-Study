
from django.shortcuts import render
import math

def bmi_in(request):
    return render(request, 'utils/bmi_in.html')

def bmi_out(request):
    #request.GET 으로 받은 html이 도착
    height = float(request.POST['height'])
    weight = float(request.POST['weight'])

    bmi = weight /(height/100) ** 2
    bmi = round(bmi, 1)

    if bmi < 18.5:
        status = 'low'
    elif bmi < 23:
        status = 'normal'
    elif bmi < 25:
        status = 'fat'
    else:
        status = 'too fat'

    return render(request, 'utils/bmi_out.html', {
        'BMI' : bmi,
        'STATUS' : status
    })