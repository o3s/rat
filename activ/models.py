from __future__ import unicode_literals
from django import forms
from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse
# Create your models here.

class Types(models.Model):
    #class Meta():
        #db_table = 'activ_type'
        #app_label = 'activ'
    types = models.CharField(max_length=250, verbose_name ='Типы активов')
    def __str__(self):
        return '%s' % self.types
    
    class Meta:
        verbose_name = "Тип актива"
        verbose_name_plural = "Типы активов"


class Rating_c(models.Model):
    #class Meta():
        #db_table =  'rating_c'
        #app_label = 'activ'
    rating = models.CharField(max_length=100, verbose_name ='Оценка конфиденциальности')
    value = models.IntegerField(default=0, verbose_name ='Значение')
    def __str__(self):
        return '%s' % self.rating
    
    class Meta:
        verbose_name = "Конфиденциальность"
        verbose_name_plural = "Конфиденциальность"


class Rating_i(models.Model):
    #class Meta():
       # db_table =  'rating_i'
       # app_label = 'activ'
    rating = models.CharField(max_length=100, verbose_name ='Оценка целостности')
    value = models.IntegerField(default=0, verbose_name ='Значение')
    def __str__(self):
        return '%s' % self.rating
    class Meta:
        verbose_name = "Целостность"
        verbose_name_plural = "Целостность"
        
class Rating_a(models.Model):
    #class Meta():
        #db_table =  'rating_a'
        #app_label = 'activ'
    rating = models.CharField(max_length=100, verbose_name ='Оценка доступности')
    value = models.IntegerField(default=0, verbose_name ='Значение')
    def __str__(self):
        return '%s' % self.rating
        
    class Meta:
        verbose_name = "Доступность"
        verbose_name_plural = "Доступность"
    
class Location (models.Model):
   # class Meta():
       # db_table =  'location'
        #app_label = 'activ'
    location = models.CharField(max_length=50, verbose_name ='Местоположение')
    group = models.CharField(max_length=100, verbose_name ='Группа')
    def __str__(self):
        return '%s %s' % (self.location, self.group)
    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположение"
    
class Activ (models.Model):
    #class Meta():
       # db_table = 'activ'
        #app_label = 'activ'
    name = models.CharField(max_length=250, verbose_name ='Имя актива')
    desc = models.TextField(verbose_name ='Описание актива')
    types = models.ForeignKey(Types, verbose_name ='Тип актива')
    owner = models.CharField(max_length=200, verbose_name ='Владелец актива')
    rating_c = models.ForeignKey(Rating_c, verbose_name ='Конфиденциальность')
    rating_i = models.ForeignKey(Rating_i, verbose_name ='Целостность')
    rating_a = models.ForeignKey(Rating_a, verbose_name ='Доступность')
    location = models.ForeignKey(Location, verbose_name ='Местоположение')
    created = models.DateTimeField(auto_now_add=True)
    
    #def get_absolute_url(self):
        #from django.core.urlresolvers import reverse
        #return "/activ/%i" % self.id
    def get_absolute_url(self):
        return reverse("activ:activ_details", kwargs={"activ_id": self.id})
    
    class Meta:
        verbose_name = "Актив"
        verbose_name_plural = "Активы"
        ordering = ["-created"]



