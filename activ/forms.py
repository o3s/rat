from django import forms
from .models import *
from django import forms
from django.forms import ModelForm

# форма создания актива
class ActivForm(forms.ModelForm):
    class Meta:
        model = Activ
        fields = ['name', 'desc', 'types', 'owner', 'rating_c', 'rating_i', 'rating_a', 'location']
        
# форма cписка активов
class ActivList(forms.ModelForm):
    class Meta:
        model = Activ;
        fields = ['id', 'name', 'desc', 'types', 'owner', 'rating_c', 'rating_i', 'rating_a', 'location' ]
        
# форма редактирования актива
class ActivEdit(ModelForm):
    class Meta:
        model = Activ
        fields = ['id', 'name', 'desc', 'types', 'owner', 'rating_c', 'rating_i', 'rating_a', 'location' ]


