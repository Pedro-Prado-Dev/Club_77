from django.shortcuts import render

def homepage(request):
    return render(request, 'página_principal/pagina_principal.html')