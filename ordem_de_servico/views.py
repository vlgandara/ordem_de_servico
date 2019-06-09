from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'ordem_de_servico/post_list.html', {})
