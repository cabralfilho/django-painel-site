from django.shortcuts import render
from .models import Servico


def servicos(request):
    context = {
        'servicos': Servico.objects.order_by('titulo').all()
    }
    return render(request, 'servicos/index.html', context)
