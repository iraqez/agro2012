from django.contrib import admin
from .models import New, Tag, Category
from sorl.thumbnail.admin import AdminImageMixin


class NewAdmin(AdminImageMixin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'get_thumbnail_html', ]
    list_display_links = ['title', ]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(New, NewAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)