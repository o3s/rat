from django.shortcuts import render
from django.http import Http404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from activ.models import *
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.forms.models import inlineformset_factory
from django.forms import formset_factory

# Create your views here.
def activ_list(request):
    filter = ActivFilter(request.GET, queryset=Activ.objects.all())
    return render(request, 'Templates/activ_list.html', {'filter': filter})

#Сождание актива
def activ_add(request):
    if request.method == "GET": 
        form = ActivForm();
        return render(request, 'Templates/activ_add.html', {'form':form });
    elif request.method == "POST":
        form = ActivForm(request.POST)
        form.save()
        return HttpResponseRedirect('/activ') 

#Детали актива
def activ_details(request,activ_id):
    try:
        activ = Activ.objects.get(pk=activ_id)
        location = Location.objects.get(pk=activ_id)
        rating_a = Rating_a.objects.get(pk=activ_id)
        rating_i = Rating_i.objects.get(pk=activ_id)
        rating_c = Rating_c.objects.get(pk=activ_id)
        types = Types.objects.get(pk=activ_id)
    except Activ.DoesNotExist:
        raise Http404("Activ does not exist")
    context = {
        'activ': activ,
        'location': location,
        'rating_a': rating_a,
        'rating_i': rating_i,
        'rating_c':rating_c,
        'types': types,
    }
    return render(request, 'Templates/activ_id.html', context)

#Редактирование актива
def activ_edit(request, activ_id):
    ActivFormSet = formset_factory(Activ)
    if request.method == 'POST':
        formset = ActivFormSet(request.POST)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            formset.save()
            return HttpResponseRedirect('/activ/activ_id')
    else:
        formset = ActivFormSet()
    return render(request, 'Templates/activ_edit.html', {'formset': formset})











#def activ_edit(request, activ_id, redirect_notice=None):
    #login stuff . . .
    #c = {}
    #c.update(csrf(request))
    #c.update({'redirect_notice':redirect_notice})#Redirect notice is an optional argument I use to send user certain notifications, unrelated to this inlineformset_factory example, but useful.

    #Intialization --- The start of the view specific functions
    #NestedFormset = inlineformset_factory(Activ, Location, Rating_i, Rating_c, Types)
    #main = None
    #if activ_id :
    #   main = Main.objects.get(id=activ_id)#get_object_or_404 is also an option

    # Save new/edited Forms
    #if request.method == 'POST':
    #    main_form = MainForm(request.POST, instance=main, prefix='mains')
    #    formset = NestedFormset(request.POST, request.FILES, instance=main, prefix='nesteds')
    #    if main_form.is_valid() and formset.is_valid():
    #        r = main_form.save(commit=False)
    #        #do stuff, e.g. setting any values excluded in the MainForm
    #        formset.save()
    #        r.save()
    #        return HttpResponseRedirect('/activ/{{activ_id}}')
    #else:
    #    main_form = MainForm(instance=main, prefix='mains') #initial can be used in the MainForm here like normal.
    #    formset = NestedFormset(instance=main, prefix='nesteds')
    #c.update({'main_form':main_form, 'formset':formset, 'realm':realm, 'main_id':main_id})
    #return render_to_response('App_name/Main_nesteds.html', c, context_instance=RequestContext(request))


#def activ_edit(request,activ_id):
#    if request.method == "GET": 
#       form = ActivEdit()
#       return render(request, 'Templates/activ_edit.html', { 'form':form })
#   elif request.method == "POST":
#        form = ActivEdit(request.POST)
#        form.save()
#        return HttpResponseRedirect('/activ/{{activ_id}}');
#        #return HttpResponseRedirect('/activ_id')
        
    #activ = get_object_or_404(Activ, pk=activ_id)
    #return render(request,'Templates/activ_id.html', {'activ': activ})
    
    #return render(request, 'Templates/activ_id.html', {})