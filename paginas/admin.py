from django.contrib import admin
from django import forms
from .models import Pagina


class PaginasAdminForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Pagina
        widgets = {
            'resumo': forms.Textarea(attrs={'class': 'vLargeTextField', 'rows': 3})
        }


class PaginasAdmin(admin.ModelAdmin):
    form = PaginasAdminForm
    prepopulated_fields = {"slug": ("titulo",)}
    list_display = ['titulo', 'slug']


admin.site.register(Pagina, PaginasAdmin)
