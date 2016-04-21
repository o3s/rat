from django.shortcuts import render, render_to_response, redirect
from django.http import Http404, HttpResponseForbidden
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
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

# Список активов
def activ_list(request):
    activ = Activ.objects.all()
    paginator = Paginator(activ, 50)
    page = request.GET.get('page')
    try:
        activs= paginator.page(page)
    except PageNotAnInteger:
        activs= paginator.page(1)
    except EmptyPage:
        activs= paginator.page(paginator.num_pages)
    return render(request, 'Templates/activ_list.html', {'activs': activs})

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
	