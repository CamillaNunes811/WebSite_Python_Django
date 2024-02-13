from django.shortcuts import render, redirect
from .models import contacto
from .forms import contactoForm

def home(request):
    return render(request,'home.html')
def destinos(request):
    return render(request,'destinos.html')
def roteiros (request):
    return render(request,'roteiros.html')


def criar_contato(request):
    if request.method == 'POST':
        form = contactoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('sucesso') 
    else:
        form = contactoForm()
    return render(request, 'contacto.html', {'form': form})

