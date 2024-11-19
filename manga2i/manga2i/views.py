from django.core.paginator import Paginator
from django.shortcuts import render
from .services.api import get_mangas, get_manga_by_id
from django.shortcuts import redirect
from django.urls import reverse

def manga_list(request, page):

    mangas = get_mangas(20*(page-1))
    
    context = {
        'page': page,
        'mangas': mangas
    }
    
    return render(request, 'manga/manga_list.html', context)

def manga_detail(request, manga_id):
    manga = get_manga_by_id(manga_id)
    return render(request, 'manga/manga_detail.html', {'manga': manga})

def manga_list_init(request):
    return redirect(reverse('manga_list', kwargs={'page': 1}))