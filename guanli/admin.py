from django.contrib import admin
from .models import Yonghu

class Yonghuadmin(admin.ModelAdmin):
    list_display = ('username','password')
admin.site.register(Yonghu,Yonghuadmin)
