from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic as views

from Miniature_market.main.forms import AddItemsToCartForm, BuyItemsForm
from Miniature_market.main.models import ShopItem, BoughtItem

UserModel = get_user_model()


class HomePageView(views.TemplateView):
    template_name = 'main/index.html'


class ShopPageView(views.ListView):
    model = ShopItem
    template_name = 'main/shop.html'
    context_object_name = 'shop_items'


def shop_item_details_view(request, pk):
    shop_item = ShopItem.objects.get(pk=pk)
    seller = get_user_model().objects.get(pk=shop_item.seller_id)

    if request.method == 'POST':
        form = AddItemsToCartForm(request.POST, instance=shop_item, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('cart page')
    else:
        form = AddItemsToCartForm(instance=shop_item, user=request.user)

    context = {
        'shop_item': shop_item,
        'seller': seller,
        'form': form
    }

    return render(request, 'main/product-details.html', context=context)


class AboutUsPageView(views.TemplateView):
    template_name = 'main/about_us.html'



@login_required()
def cart_page_view(request):
    bought_items = list(BoughtItem.objects.filter(buyer_id=request.user.pk))
    if request.method == 'POST':
        form = BuyItemsForm(request.POST, instance=None, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = BuyItemsForm(instance=None, user=request.user)
    context = {
        'bought_items': bought_items,
        'form': form
    }
    return render(request, 'main/shop-cart.html', context=context)
