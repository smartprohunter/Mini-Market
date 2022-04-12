from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from Miniature_market.accounts.models import Profile, MarketUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ProfileAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs



@admin.register(MarketUser)
class MarketUserAdmin(BaseUserAdmin):
    add_form = UserCreationForm

    list_display = ('username',)
    list_filter = ('is_active', 'groups', 'is_superuser')

    fieldsets = (
        (None,
         {'fields': ('username', 'password',  'is_staff', 'is_superuser', 'groups', )}),


    )
    search_fields = ('username',)
    ordering = ('username',)

    filter_horizontal = ()
