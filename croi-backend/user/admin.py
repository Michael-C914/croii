from django.contrib import admin

from user.models import CustomUser, SpecialUser, UserJuridic, UserNatural
from rest_framework_simplejwt.token_blacklist import models as token_models
from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(SpecialUser)
admin.site.register(UserJuridic)
admin.site.register(UserNatural)


class NewOutstandingTokenAdmin(OutstandingTokenAdmin):

    def has_delete_permission(self, *args, **kwargs):
        return True  # or whatever logic you want


admin.site.unregister(token_models.OutstandingToken)
admin.site.register(token_models.OutstandingToken,
                    NewOutstandingTokenAdmin)
