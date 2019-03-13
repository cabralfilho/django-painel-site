from django.contrib import admin
from imagekit.admin import AdminThumbnail
from .models import Banner


class BannersAdmin(admin.ModelAdmin):
    admin_thumbnail = AdminThumbnail(image_field='thumbnail_horizontal')
    list_display = ['descricao', 'link', 'is_blank', 'admin_thumbnail']
    list_editable = ['link', 'is_blank']


admin.site.register(Banner, BannersAdmin)
