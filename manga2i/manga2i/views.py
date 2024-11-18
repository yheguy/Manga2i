from django.core.paginator import Paginator
from django.shortcuts import render
from .services.api import get_mangas, get_manga_by_id

def manga_list(request):
    page_number = int(request.GET.get('page', 1))
    
    mangas = get_mangas(20*(page_number-1))
    
    paginator = Paginator(mangas, 20)
    
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'manga/manga_list.html', {'page_obj': page_obj})

def manga_detail(request, manga_id):
    manga = get_manga_by_id(manga_id)
    return render(request, 'manga/manga_detail.html', {'manga': manga})