from django import forms

from Miniature_market.common.helpers import BootstrapFormMixin
from Miniature_market.main.models import ShopItem, BoughtItem


class CreateShopItemForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        shop_item = super().save(commit=False)
        shop_item.seller_id = self.user.pk
        if commit:
            shop_item.save()

        return shop_item

    class Meta:
        model = ShopItem
        fields = ('name', 'type', 'image', 'price', 'description')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter  name',
                }
            ),

        }


class DeleteShopItemForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        fields = ()
        model = ShopItem


class AddItemsToCartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.buyer = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        item = super().save(commit=commit)

        bought_item = BoughtItem(

            name=item.name,
            type=item.type,
            price=item.price,
            image=item.image,
            buyer_id=self.buyer.pk,

        )

        if commit:
            bought_item.save()
            self.instance.delete()
        return item

    class Meta:
        fields = ()
        model = ShopItem


class BuyItemsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.buyer = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        BoughtItem.objects.filter(buyer_id=self.buyer.pk).delete()

    class Meta:
        model = BoughtItem
        fields = ()