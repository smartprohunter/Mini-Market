from django.contrib.auth import get_user_model

from Miniature_market.main.models import ShopItem, BoughtItem

UserModel= get_user_model()
class ValidDataMixin:
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': '1234HaGHA',
    }

    VALID_SECOND_USER_CREDENTIALS = {
        'username': 'testUser',
        'password': '1234HaGHA',
    }
    VALID_SHOP_ITEM_DATA = {
        'name': 'name',
        'image': 'download_KcjNGqi.jpg',
        'price': '45',
        'type': ShopItem.CHAOS_SPACE_MARINES,

    }
    Valid_BOUGHT_ITEM_DATA = {
        'name': 'name',
        'image': 'download_KcjNGqi.jpg',
        'price': '45',
        'type': ShopItem.CHAOS_SPACE_MARINES,

    }
    def _create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)

    def _create_shop_item(self, user):
        shop_item = ShopItem.objects.create(
            **self.VALID_SHOP_ITEM_DATA,
            seller_id=user,
        )
        return shop_item

    def _create_bought_item(self, user):
        shop_item = BoughtItem.objects.create(
            **self.Valid_BOUGHT_ITEM_DATA,
            buyer_id=user,
        )
        return shop_item