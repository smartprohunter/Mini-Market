from django.contrib import admin

# Register your models here.
from Miniature_market.main.models import ShopItem, BlogPost


@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass