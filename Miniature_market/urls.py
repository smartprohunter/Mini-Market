from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Miniature_market.accounts.urls')),
    path('', include('Miniature_market.main.urls')),
]
