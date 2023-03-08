from django.contrib import admin

# Register your models here.
from . models import National, ExtraCounty, County, Result, School, SubCounty

admin.site.register(School)
admin.site.register(National)
admin.site.register(ExtraCounty)
admin.site.register(County)
admin.site.register(SubCounty)
admin.site.register(Result)
