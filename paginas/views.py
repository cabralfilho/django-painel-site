from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
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
    form_submitted = False;

    if request.method == 'GET':
        form = FormularioContato()
    else:
        # Envio de email
        form_submitted = True
        form = FormularioContato(request.POST)
        if form.is_valid():
            mensagem = 'Nome: ' + form.cleaned_data['nome']
            mensagem += '\nE-mail: ' + form.cleaned_data['email']
            mensagem += '\nTelefone: ' + form.cleaned_data['telefone']
            mensagem += '\nMensagem: ' + form.cleaned_data['mensagem']
            send_mail(
                'Formulário de contato',
                mensagem,
                form.cleaned_data['email'],
                ['richellyitalo@gmail.com']
            )
            return redirect('contato')

    context = {
        'form': form,
        'form_submitted': form_submitted
    }
    return render(request, 'paginas/contato.html', context)
