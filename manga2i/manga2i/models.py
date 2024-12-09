from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    manga_id = models.CharField(max_length=255)  
    quantity = models.PositiveIntegerField(default=0)

@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)