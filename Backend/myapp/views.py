from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Piloto, Noticia

#crie suas views aqui
def main(request):
    return render(request, 'main.html')

def news(request):
    return render(request, 'news.html')

def results(request):
    return render(request, 'results.html')

def drivers(request):
    pilotos = Piloto.objects.all()
    return render(request, 'drivers.html', {'pilotos': pilotos})

def teams(request):
    return render(request, 'teams.html')

def tracks(request):
    return render(request, 'tracks.html')


@login_required
def saveNews(request):
    if request.method == 'POST':
        title = request.POST.get('titleNews')
        content = request.POST.get('contentNews')
        print(title)
        
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

@login_required
def saveDriver(request):
    if request.method == 'POST':
        nome = request.POST.get('nameDriver')
        equipe = request.POST.get('team')
        dataNasc = request.POST.get('dateDriver')
        numeracao = request.POST.get('numberDriver')
        pais = request.POST.get('country')
        foto = request.FILES.get('imageDriver')
        print(nome, equipe, dataNasc, numeracao, pais, foto)

        try:
            piloto = Piloto.objects.create(
                pilotoNome=nome,
                pilotoEquipe=equipe,
                pilotoDataNasc=dataNasc,
                pilotoNumeracao=numeracao,
                pilotoPais=pais,
                pilotoFoto=foto
            )
            print('Piloto criado com sucesso: ', piloto)
            return JsonResponse({'success': True, 'id': piloto.id})
        except Exception as e:
            return JsonResponse({'sucess': False, 'error':str(e)}, status=400)
    return JsonResponse({'success': False, 'error': str(e)}, status=400)
