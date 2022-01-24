from django.contrib import admin

from user.models import CustomUser, SpecialUser, UserJuridic, UserNatural

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(SpecialUser)
admin.site.register(UserJuridic)
admin.site.register(UserNatural)
