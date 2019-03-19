from django.shortcuts import render, get_object_or_404
from .models import Pagina
from banners.models import Banner
from servicos.models import Servico
from capacidades.models import Capacidade
from membros.models import Membro
from depoimentos.models import Depoimento
from clientes.models import Cliente
from paginas.forms import FormularioContato


def pagina(request, slug):
    pagina_object = get_object_or_404(Pagina, slug=slug)
    return render(request, 'paginas/pagina.html', {'pagina': pagina_object})


def home(request):
    banners     = Banner.objects.order_by('-id').all()[:5]
    servicos    = Servico.objects.order_by('titulo').all()[:4]
    capacidades = Capacidade.objects.order_by('titulo').all()
    membros     = Membro.objects.order_by('nome').all()
    depoimentos = Depoimento.objects.order_by('?').all()[:4]
    clientes    = Cliente.objects.order_by('?').all()[:6]

    context = {
        'banners'    : banners,
        'servicos'   : servicos,
        'capacidades': capacidades,
        'membros'    : membros,
        'depoimentos': depoimentos,
        'clientes'   : clientes
    }

    return render(request, 'paginas/home.html', context)


def contato(request):
    if request.method == 'GET':
        form = FormularioContato()
    else:
        form = FormularioContato(request.POST)
        if form.is_valid():
            # Enviar email
            print('enviar_email')

    context = {
        'form': form
    }
    return render(request, 'paginas/contato.html', context)
