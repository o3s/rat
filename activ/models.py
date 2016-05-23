from __future__ import unicode_literals
from django import forms
from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse
import django_filters
from django_filters import filters
import django_tables2 as tables
from django_tables2.utils import A

# Create your models here.

class Types(models.Model):
    TYPES_CHOICES=(
        (0, u'Бумажный документ'),
        (1, u'Электронный документ'),
        (2, u'Физический сервер'),
        (3, u'Виртуальный сервер'),
        (4, u'Канал связи'),
        (5, u'Мобильное устройство'),
        (6, u'Ноутбук'),
        (7, u'Оборудование'),
        (8, u'Персонал'),
        (9, u'Помещение'),
        (10, u'Печатающее устройство'),
        (11, u'Программный'),
        (12, u'Сервис'),
        (13, u'Сетевое оборудование'),
        (14, u'Сканер'),
        (15, u'Стационарный компьютер'),
        (16, u'Телефония'),
        (17, u'Электронный носитель'),
        )
    types = models.IntegerField(verbose_name ='Типы активов', choices=TYPES_CHOICES)
    def __str__(self):
        return '%s' % self.types
    
    class Meta:
        ordering = ('types',)
        verbose_name = "Тип актива"
        verbose_name_plural = "Типы активов"


class Rating_c(models.Model):
  
    rating = models.CharField(max_length=100, verbose_name ='Оценка конфиденциальности')
    value = models.IntegerField(default=0, verbose_name ='Значение')
    def __str__(self):
        return '%s' % self.rating
    
    class Meta:
        ordering = ('value',)
        verbose_name = "Конфиденциальность"
        verbose_name_plural = "Конфиденциальность"


class Rating_i(models.Model):
    rating = models.CharField(max_length=100, verbose_name ='Оценка целостности')
    value = models.IntegerField(default=0, verbose_name ='Значение')
    def __str__(self):
        return '%s' % self.rating
    class Meta:
        ordering = ('value',)
        verbose_name = "Целостность"
        verbose_name_plural = "Целостность"
        
class Rating_a(models.Model):
    rating = models.CharField(max_length=100, verbose_name ='Оценка доступности')
    value = models.IntegerField(default=0, verbose_name ='Значение')
    def __str__(self):
        return '%s' % self.rating

    class Meta:
        ordering = ('value',)
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
    name = models.CharField(max_length=250, verbose_name ='Актив')
    desc = models.TextField(verbose_name ='Описание актива')
    types = models.ForeignKey(Types, verbose_name ='Тип актива')
    owner = models.CharField(max_length=200, verbose_name ='Владелец актива')
    rating_c = models.ForeignKey(Rating_c, verbose_name ='Конфиденциальность')
    rating_i = models.ForeignKey(Rating_i, verbose_name ='Целостность')
    rating_a = models.ForeignKey(Rating_a, verbose_name ='Доступность')
    location = models.ForeignKey(Location, verbose_name ='Местоположение')
    created = models.DateTimeField(auto_now_add=True, verbose_name ='Создан')
    def _get_total(self):
       "Returns the total"
       return Rating_a.value+Rating_c.value+Rating_i.value
    total = property(_get_total) 
    
    #def get_absolute_url(self):
        #from django.core.urlresolvers import reverse
        #return "/activ/%i" % self.id
    def get_absolute_url(self):
        return reverse("activ:activ_details", kwargs={"activ_id": self.id})
    
    class Meta:
        verbose_name = "Актив"
        verbose_name_plural = "Активы"
        ordering = ["-created"]


# класс для создания таблицы через django_tables2
class ActivTable(tables.Table):
    name = tables.LinkColumn("activ:activ_details", args=[A('id')])
    class Meta:
        model = Activ
        fields = ("id","name","desc","types","owner","rating_c","rating_i","rating_a","location",)
        attrs = {"class":"table table-striped"}


