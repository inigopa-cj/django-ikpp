from django.contrib import admin
from .models import RRSS

# Register your models here.
class RRSSAdmin(admin.ModelAdmin):
    pass

admin.site.register(RRSS, RRSSAdmin)