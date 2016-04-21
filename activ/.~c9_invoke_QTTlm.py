from django.shortcuts import render
from django.http import Http404
from .models import activ
# Create your views here.
def activ_list(request):
    return render(request, 'Templates/activ_list.html', {})

def activ_details(request, act_id):
    activ = Activ.objects.get(pk = act_id);
    return render_to_response('Templates/activ_id.html', {'activ': activ});
    
    #return render(request, 'Templates/activ_id.html', {})