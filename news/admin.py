from django.contrib import admin
from .models import New
from sorl.thumbnail.admin import AdminImageMixin

class NewAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

admin.site.register(New, NewAdmin)
