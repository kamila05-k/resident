from django.contrib import admin
from .models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ('blog', 'ratation', 'date')
    list_filter = ('date',)
    ordering = ('date',)

admin.site.register(Banner, BannerAdmin)
