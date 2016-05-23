from django.shortcuts import render, render_to_response, redirect
from django.http import Http404, HttpResponseForbidden
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import RequestContext
from datetime import datetime
from activ.models import *
from activ.forms import *
from django.shortcuts import get_object_or_404,  get_list_or_404
from django.forms.models import inlineformset_factory
from django.forms import formset_factory
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django_tables2 import RequestConfig
from django.db.models import Count


# Список активов
def activ_list(request):
    activ = Activ.objects.all()
    table = ActivTable(activ)
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get('page', 1), per_page=50)
    return render(request, 'Templates/activ_list.html', {'table': table})

# Детали одного актива
def activ_details(request, activ_id):
    try:
        activ = Activ.objects.get(pk=activ_id)
    except Activ.DoesNotExist:
        raise Http404("Activ does not exist")
    activ = Activ.objects.get(pk = activ_id)
    return render_to_response('Templates/activ_id.html', { 'activ': activ })

#Сождание актива
def activ_add(request):
    if request.method == "GET": 
        form = ActivForm();
        return render(request, 'Templates/activ_add.html', {'form':form });
    elif request.method == "POST":
        form = ActivForm(request.POST)
        form.save()
        return HttpResponseRedirect('/activ') 

#Редактирование актива
def activ_edit(request, activ_id =None):
    instance = get_object_or_404(Activ, id = activ_id)
    form = ActivEdit(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request,'Templates/activ_edit.html', {
        'form': form,
        })
# Удаление актива
def activ_del(request, activ_id=None):
    instance = get_object_or_404(Activ,  id= activ_id).delete()
    return redirect('activ:activ')
	
# Создание дашбордов
# Дашборд по статистике активов активов 
def activ_dash(request):
    """
    pieChart по типу активов
    """
    xdata = [u'Бумажный документ', u'Электронный документ', u'Физический сервер', u'Виртуальный сервер', u'Канал связи',
             u'Мобильное устройство', u'Ноутбук', u'Оборудование', u'Персонал', u'Помещение', u'Печатающее устройство',
             u'Программный', u'Сервис', u'Сетевое оборудование', u'Сканер', u'Стационарный компьютер', u'Телефония', u'Электронный носитель' ]
    
    ydata = [Activ.objects.filter(types=x).count() for x in range(17)]
    
    color_list = ['#5d8aa8', '#e32636', '#efdecd', '#ffbf00', '#ff033e', '#a4c639',
                  '#b2beb5', '#8db600', '#7fffd4', '#ff007f', '#ff55a3', '#5f9ea0',
                  '#0099ff', '#cc66ff', '#cc33ff', '#ff6699', '#ffff00', '#99ff33',
                  ]
    extra_serie = {
        "tooltip": {"y_start": "", "y_end": "ед"},
        "color_list": color_list,
    }
    chartdata = {'x': xdata, 'y': ydata, 'extra': extra_serie}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'  # container name
    """
    Дашборд pieChart по ТОП 5 владельцев активов
    """
    #xdata11= Activ.objects.values('owner').annotate(activ_count=Count('id')).order_by('-activ_count')[:5]
    xdata1= Activ.objects.values('owner').annotate(activ_count=Count('id')).order_by('-activ_count').values_list('owner')[:5]
   
    ydata1 = Activ.objects.values('owner').annotate(activ_count=Count('id')).order_by('-activ_count').values_list('activ_count')[:5]

    color_list1 = ['#5d8aa8', '#e32636', '#efdecd', '#ffbf00', '#ff033e',
                  ]
    extra_serie1 = {
        "tooltip": {"y_start": "", "y_end": "ед"},
        "color_list": color_list1
    }
    chartdata1 = {'x': xdata1, 'y': ydata1, 'extra': extra_serie1}
    charttype1 = "pieChart"
    chartcontainer1 = 'piechart_container1'# container name
    """
    pieChart по месту расположения активов
    """
    xdata22= Activ.objects.values('location').annotate(activ_count=Count('id')).order_by('-activ_count').values_list('location')
    xdata2= [Location.id(x) for x in xdata22]
   
    ydata2 = Activ.objects.values('location').annotate(activ_count=Count('id')).order_by('-activ_count').values_list('activ_count')

   
    extra_serie2 = {
        "tooltip": {"y_start": "", "y_end": "ед"},
       }
    chartdata2 = {'x': xdata2, 'y': ydata2, 'extra': extra_serie2}
    charttype2 = "pieChart"
    chartcontainer2 = 'piechart_container2'# container name
    
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        },
        'charttype1': charttype1,
        'chartdata1': chartdata1,
        'chartcontainer1': chartcontainer1,
        'extra1': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        },
        'charttype2': charttype2,
        'chartdata2': chartdata2,
        'chartcontainer2': chartcontainer2,
        'extra2': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('Templates/activ_dash.html', data)
    

