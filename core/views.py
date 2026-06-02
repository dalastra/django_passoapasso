from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Contato
from .forms import ContatoForm


# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def contatos_json(request):
    contatos = list(Contato.objects.values('id', 'nome', 'email', 'mensagem', 'imagem', 'criado_em'))
    return JsonResponse({'contatos': contatos})

def contatos_lista(request):
    contatos = Contato.objects.all().order_by('-criado_em')
    return render(request, 'core/contatos_lista.html', {'contatos': contatos})

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = ContatoForm()

    return render(request, 'core/contato.html', {'form': form})


def sucesso(request):
    return render(request, 'core/sucesso.html')