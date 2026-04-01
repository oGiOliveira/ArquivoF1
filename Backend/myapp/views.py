from django.shortcuts import render

#crie suas views aqui
def newsPage(request):
    return render(request, 'news.html')
