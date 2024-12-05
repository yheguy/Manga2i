from copy import deepcopy

from django.db import models


class Manga(models.Model):
    id = models.CharField(primary_key=True, max_length=50) 
    title = models.CharField(max_length=200, default="manga title")  
    description = models.TextField(default="description")  
    original_language = models.CharField(max_length=50, default="japanese")  
    last_volume = models.CharField(max_length=50, null=True, blank=True)  
    last_chapter = models.CharField(max_length=50, null=True, blank=True)  
    status = models.CharField(max_length=50, blank=True)  
    year = models.IntegerField(blank=True) 
    grade = models.FloatField(blank=True) 
    url_cover = models.URLField(blank=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2, default=6.99)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title

"""

@dataclass
class Stock:
    articles: list[Manga]

    def copy(self):
        return deepcopy(self)

    def add_article(self, article):
        if all(a.code != article.code for a in self.articles):
            self.articles.append(article)
            self.articles.sort(key=lambda x: x.code)  

    def get_stock(self, code):
        for article in self.articles:
            if article.code == code:
                return article.quantite
        return None

    def supprime_article(self, code):
        for i, article in enumerate(self.articles):
            if article.code == code:
                del self.articles[i]
                return True
        return False
    
    def fusion(self, other_stock):
        new_stock = self.copy()
        for article in other_stock.articles:
            found = False
            for existing_article in new_stock.articles:
                if existing_article.code == article.code:
                    nom_combine = (existing_article.nom if existing_article.nom == article.nom 
                                   else f"{existing_article.nom}_{article.nom}")
                    existing_article.nom = nom_combine
                    existing_article.quantite += article.quantite
                    existing_article.unite_vente = min(existing_article.unite_vente, article.unite_vente)
                    found = True
                    break
            if not found:
                new_stock.articles.append(article)

        new_stock.articles.sort(key=lambda x: x.code) 
        return new_stock

    def affiche_stock(self):
        if not self.articles:
            print("Le stock est vide.")
        for article in self.articles:
            article.affiche()

    def approvisionner(self, code, quantite):
        for article in self.articles:
            if article.code == code:
                article.add_stock(quantite)
                return True
        return False

    def vente(self, code, quantite):
        for article in self.articles:
            if article.code == code:
                if quantite % article.unite_vente == 0:
                    if article.quantite >= quantite:
                        article.quantite -= quantite
                        return True
                    else:
                        print("stock insuffisant")
                else:
                    print("quantité pas valable a cause de l'unité de vente")
        return False
    
@dataclass
class panier:

    id_user: str
    panier: Stock

"""