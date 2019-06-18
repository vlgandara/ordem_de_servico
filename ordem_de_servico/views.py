from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Equipamento, OrdemServico
from .forms import PostForm, OrdemForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
    equipments = Equipamento.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'ordem_de_servico/post_list.html', {'equipments': equipments})

def equipment_new(request):
    if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             equipment = form.save(commit=False)
             equipment.published_date = timezone.now()
             equipment.save()
             return redirect('equipment_detail', pk=equipment.pk)
    else:
        form = PostForm()
    return render(request, 'ordem_de_servico/equipment_edit.html', {'form': form})

def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipamento, pk=pk)
    return render(request, 'ordem_de_servico/equipment_detail.html', {'equipment': equipment})

def ordem_list(request):
    ordens = OrdemServico.objects.filter(datasolicitacao__lte=timezone.now()).order_by('datasolicitacao') 
    return render(request, 'ordem_de_servico/ordem_list.html', {'ordens': ordens})

def ordem_new(request):
    if request.method == "POST":
         form = OrdemForm(request.POST)
         if form.is_valid():
             ordem = form.save(commit=False)
             ordem.datasolicitacao = timezone.now()
             ordem.save()
             return redirect('ordem_detail', pk=ordem.pk)

    else:
        form = OrdemForm()
    return render(request, 'ordem_de_servico/ordem_edit.html', {'form': form})

def ordem_detail(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)
    return render(request, 'ordem_de_servico/ordem_detail.html', {'ordem': ordem})

