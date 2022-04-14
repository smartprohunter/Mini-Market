from django.contrib import admin
from django.urls import path, include

PAGE_NOT_FOUND_VIEW_LOCATION = 'Miniature_market.main.views.exceptions.error_404_view'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Miniature_market.accounts.urls')),
    path('', include('Miniature_market.main.urls')),
]
handler404 = PAGE_NOT_FOUND_VIEW_LOCATION
