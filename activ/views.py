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
from django_tables2   import RequestConfig

from chartit import DataPool, Chart
from unit.analysis_funcs import ChartData

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
def demo_piechart(request):
    """
    pieChart page
    """
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries",
             "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]

    color_list = ['#5d8aa8', '#e32636', '#efdecd', '#ffbf00', '#ff033e', '#a4c639',
                  '#b2beb5', '#8db600', '#7fffd4', '#ff007f', '#ff55a3', '#5f9ea0']
    extra_serie = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "color_list": color_list
    }
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'  # container name

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('piechart.html', data)
    
    
