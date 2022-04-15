from http import HTTPStatus

from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from Miniature_market.accounts.models import MarketUser
from Miniature_market.main.models import ShopItem
from Miniature_market.main.tests.mixins_for_testing import ValidDataMixin

UserModel = get_user_model()


class ShopDetailsViewTests(ValidDataMixin, django_test.TestCase):

    def _create_user(self, **kwargs):
        return MarketUser.objects.create_user(**kwargs)

    def test_get_right_template(self):
        print(MarketUser)

        seller = self._create_user(**self.VALID_USER_CREDENTIALS)
        buyer = self._create_user(**self.VALID_SECOND_USER_CREDENTIALS)
        shop_item = self._create_shop_item(seller)
        response = self.client.get(reverse('shop details page', shop_item.pk))

        self.assertTemplateUsed(response, 'main/product-details.html')
