from django.shortcuts import render
from django.http import HttpResponse
from .models import Collection, Piece


# Create your views here.
def genre(request):
    all_collections = Collection.objects.all()
    context = {
        'all_collections': all_collections
    }
    return render(request, 'genre\\genretemplate.html', context)

def details(request, genre_id):
    Citem = Collection.objects.get(pk=genre_id)
    Pieces = Piece.objects.filter(collection=Citem)
    context = {
        'Citem': Citem,
        'Pieces': Pieces
    }
    return render(request, 'genre\\detailtemplates.html', context)