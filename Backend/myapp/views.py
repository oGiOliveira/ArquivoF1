from django.shortcuts import render

#crie suas views aqui
def main(request):
    return render(request, 'main.html')

def news(request):
    return render(request, 'news.html')

def results(request):
    return render(request, 'results.html')

def drivers(request):
    return render(request, 'drivers.html')

def teams(request):
    return render(request, 'teams.html')

def tracks(request):
    return render(request, 'tracks.html')
