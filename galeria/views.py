from django.shortcuts import render
from galeria.models import Fotografia
from django.shortcuts import render, get_object_or_404

def index(request):
    # Vai trazer a lista de objetos la do models 
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id): # foto_id vai servir para pegar os dados referente ao id dado no bd
    fotografia = get_object_or_404(Fotografia, pk = foto_id) # metodo proprio do django para mostrar a imagem ou gerar o 4040 em caso de not found
    return render(request, 'galeria/imagem.html',{"fotografia": fotografia})