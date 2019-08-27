from django.shortcuts import render

def retornar_index(request):
    return render(request, 'index.html')