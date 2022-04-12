from django.urls import reverse_lazy
from django.views import generic as views

from Miniature_market.main.forms import CreateShopItemForm, DeleteShopItemForm
from Miniature_market.main.models import ShopItem


class CreateShopItem(views.CreateView):
    model = ShopItem
    template_name = 'main/shop_item_create.html'
    success_url = reverse_lazy('home page')
    form_class = CreateShopItemForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditShopItem(views.UpdateView):
    model = ShopItem
    template_name = 'main/shop_item_edit.html'
    fields = ('description',)

    def get_success_url(self):
        return reverse_lazy('home page')


class DeleteShopItem(views.DeleteView):
    model = ShopItem
    template_name = 'main/shop_item_delete.html'
    form_class = DeleteShopItemForm
    success_url = reverse_lazy('home page')


