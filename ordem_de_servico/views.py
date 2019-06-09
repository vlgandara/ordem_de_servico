from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Equipamento
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
    equipamentos = Equipamento.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'ordem_de_servico/post_list.html', {'equipamentos': equipamentos})

def equipment_new(request):
    if request.method == "EQUIPAMENTO":
         form = PostForm(request.EQUIPAMENTO)
         if form.is_valid():
             equipamento = form.save(commit=False)
             equipamento.equipamento = request.equipamento
             equipamento.marca = request.marca
             equipamento.save()
             return redirect('equipment_detail', pk=equipamento.pk)
    else:
        form = PostForm()
    return render(request, 'ordem_de_servico/equipment_edit.html', {'form': form})

def equipment_detail(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    return render(request, 'ordem_de_servico/equipment_detail.html', {'equipamento': equipamento})
