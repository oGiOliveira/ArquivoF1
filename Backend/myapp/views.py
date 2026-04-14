from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Piloto

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


@login_required
def saveDriver(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        equipe = request.POST.get('equipe')
        dataNasc = request.POST.get('dataNasc')
        numeracao = request.POST.get('numeracao')
        pais = request.POST.get('pais')
        foto = request.FILES.get('foto')
        print(nome, equipe, dataNasc, numeracao, pais, foto)

        try:
            piloto = Piloto.objects.create(
                nome=nome,
                equipe=equipe,
                dataNasc=dataNasc,
                numeracao=numeracao,
                pais=pais,
                foto=foto
            )
            print('Piloto criado com sucesso: ', piloto)
            return JsonResponse({'success': True, 'id': transfer.id})
        except Exception as e:
            return JsonResponse({'sucess': False, 'error':str(e)}, status=400)
    return JsonResponse({'success': False, 'error': str(e)}, status=400)
