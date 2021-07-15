from django.shortcuts import render
from apps.models import *
from .forms import *

def index(request):
    form = FechasForm()
    if request.method == "GET":
        return render(request, 'index.html', {'form': form})
    else:
        form = FechasForm(request.POST)
        if form.is_valid():
            fechaI = form.cleaned_data.get("fechaInicio")
            fechaF = form.cleaned_data.get("fechaFin")
            usuarios = Usuario.objects.filter(
                departamento__fecha_bono__range=[fechaI, fechaF])
            total = 0
            for u in usuarios:
                total += u.departamento.bono
            context = {
                'form': form,
                'users': usuarios,
                'total': total,
            }
            return render(request, 'index.html', context)
