from django.shortcuts import render

# Create your views here.
def Notas(request):
    return render(request, 'notas.html')