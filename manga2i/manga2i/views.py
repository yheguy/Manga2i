from django.shortcuts import render, redirect, get_object_or_404
from .services.api import fetch_and_update_mangas
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test, login_required
from . import models as mod
from django.http import HttpResponseBadRequest, JsonResponse


def superuser_check(user):
    return user.is_superuser

@login_required(login_url='/login/')
def manga_list(request, page):

    mangas = mod.Manga.objects.order_by('-grade')[20*(page-1):20*page]
    
    context = {
        'page': page,
        'mangas': mangas
    }
    
    return render(request, 'manga/manga_list.html', context)

@login_required(login_url='/login/')
def manga_detail(request, manga_id):
    manga = mod.Manga.objects.get(id=manga_id)
    return render(request, 'manga/manga_detail.html', {'manga': manga})

@login_required(login_url='/login/')
def manga_list_init(request):
    return redirect(reverse('manga_list', kwargs={'page': 1}))

@user_passes_test(superuser_check, login_url='/login/')
def manga_stock(request, page):

    fetch_and_update_mangas(20*(page-1))
    
    mangas = mod.Manga.objects.order_by('-grade')[20*(page-1):20*page]

    context = {
        'page': page,
        'mangas': mangas
    }
    
    return render(request, 'manga/manga_stock.html', context)

@user_passes_test(superuser_check, login_url='/login/')
def manga_stock_init(request):
    return redirect(reverse('manga_stock', kwargs={'page': 1}))

@user_passes_test(superuser_check, login_url='/login/')
def update_manga(request, manga_id, page=1):
    manga = get_object_or_404(mod.Manga, id=manga_id)
    
    if request.method == 'POST':
        
        new_price = request.POST.get('new_price')
        new_stock = request.POST.get('new_stock')
        
        try:
            manga.price = float(new_price)  
            manga.stock = int(new_stock)  
            manga.save() 

            return JsonResponse({'success': True, 'new_stock': manga.stock, 'new_price': manga.price, 'title': manga.title})
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Valeurs invalides'})
        

    return JsonResponse({'success': False, 'error': 'Mauvaise requête'})