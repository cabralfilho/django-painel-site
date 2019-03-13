from django.shortcuts import render, get_object_or_404
from .models import Pagina
from banners.models import Banner
from servicos.models import Servico
from capacidades.models import Capacidade
from membros.models import Membro


def home(request):
    banners = Banner.objects.order_by('-id').all()[:5]
    servicos = Servico.objects.order_by('titulo').all()[:4]
    capacidades = Capacidade.objects.order_by('titulo').all()
    membros = Membro.objects.order_by('nome').all()

    context = {
        'banners': banners,
        'servicos': servicos,
        'capacidades': capacidades,
        'membros': membros
    }

    return render(request, 'paginas/home.html', context)


def pagina(request, slug):
    pagina_object = get_object_or_404(Pagina, slug=slug)
    return render(request, 'paginas/pagina.html', {'pagina': pagina_object})
