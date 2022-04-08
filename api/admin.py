from django.contrib import admin
from .models import Page, Link


admin.site.register(Page, admin.ModelAdmin)
admin.site.register(Link, admin.ModelAdmin)
