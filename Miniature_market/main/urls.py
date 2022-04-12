from django.conf.urls.static import static
from django.urls import path

from Miniature_market import settings
from Miniature_market.main.views.blog import BlogPageView, BlogDetailsPageView
from Miniature_market.main.views.generic import HomePageView, ShopPageView, AboutUsPageView, shop_item_details_view, \
    cart_page_view

from Miniature_market.main.views.shop_item import CreateShopItem, EditShopItem, DeleteShopItem

urlpatterns = [
                  path('', HomePageView.as_view(), name='home page'),
                  path('about/', AboutUsPageView.as_view(), name='about us page'),
                  path('shop/', ShopPageView.as_view(), name='shop page'),
                  path('shop/details/<int:pk>', shop_item_details_view, name='shop details page'),
                  path('create/', CreateShopItem.as_view(), name='create item'),
                  path('edit/<int:pk>', EditShopItem.as_view(), name='edit item'),
                  path('delete/<int:pk>', DeleteShopItem.as_view(), name='delete item'),
                  path('cart/', cart_page_view, name='cart page'),
                  path('blog/', BlogPageView.as_view(), name='blog page'),
                  path('blog/details/<int:pk>', BlogDetailsPageView.as_view(), name='blog details page')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
