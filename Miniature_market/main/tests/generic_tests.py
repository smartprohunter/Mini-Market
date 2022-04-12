from http import HTTPStatus

from django import test as django_test
from django.contrib.auth import get_user_model

from Miniature_market.main.models import ShopItem
from Miniature_market.main.tests.mixins_for_testing import ValidDataMixin

UserModel = get_user_model()


class ShopPageViewTests(django_test.TestCase):
    pass