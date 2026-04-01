from django.shortcuts import render

#crie suas views aqui
def mainPage(request):
    return render(request, 'main.html')
