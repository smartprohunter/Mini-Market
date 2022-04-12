from django import test as django_test

from Miniature_market.main.forms import BuyItemsForm, AddItemsToCartForm
from Miniature_market.main.tests.mixins_for_testing import ValidDataMixin


class BuyItemFormTest(ValidDataMixin, django_test.TestCase):
    FORM = BuyItemsForm
    def test_valid_form(self):
        seller = self._create_user(**self.VALID_USER_CREDENTIALS)
        buyer = self._create_user(**self.VALID_SECOND_USER_CREDENTIALS)
        bought_item = self._create_bought_item(buyer.pk)

        shop_item = self._create_shop_item(seller.pk)

        form = AddItemsToCartForm(instance=shop_item, user=seller)



