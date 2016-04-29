from activ.models import Activ
from unit.models import CheckValve
from django.template import RequestContext

# Создание дашбордов
#def activ_dash(request):
    
class activ_dash(request):    
    def check_activ_data():
        data = {'activ.types': [], 'ssuma': []}

        valves = Activ.objects.all()

        for activ in valves:
            count= Activ.types.objects.all().count()
            data['activ.types'].append(activ.types)
            data['ssuma'].append(count))
            
        return data      
