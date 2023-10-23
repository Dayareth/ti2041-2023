from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    if request.POST:
        operador1=request.POST['operador1']
        operador2=request.POST['operador2']
        operacion=request.POST['operacion'] 
        context={
        'operador1':operador1,
        'operador2':operador2,
                'operacion':operacion,
                    'resultado':0
                            }
        if operacion == 'suma':
            context['resultado']= operador1 + operador2    
        elif operacion == 'resta':
            context['resultado']= operador1 - operador2
        elif operacion == 'multiplicacion':
            context['resultado']= operador1 * operador2
        elif operacion == 'division':
            context['resultado']= operador1 / operador2
    
    
    return render(request,'index.html',context) 
    

# Create your views here.