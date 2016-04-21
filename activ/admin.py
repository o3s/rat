
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import os, sys
from django.contrib import admin
from django.contrib import admin


# Register your models here.
from .models import Activ, Types, Rating_c, Rating_i, Rating_a, Location

class TypesInline(admin.TabularInline):
    model = Types

class ActivAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'desc', 'types', 'owner', 'rating_c','rating_i','rating_a', 'location')
    


class TypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'types')

class Rating_cAdmin(admin.ModelAdmin):
    list_display = ('id','rating', 'value')

class Rating_iAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'value')
    
class Rating_aAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'value')    

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'group')    

admin.site.register(Activ, ActivAdmin)
admin.site.register(Types, TypesAdmin)
admin.site.register(Rating_c, Rating_cAdmin)
admin.site.register(Rating_i, Rating_iAdmin)
admin.site.register(Rating_a, Rating_aAdmin)
admin.site.register(Location, LocationAdmin)
