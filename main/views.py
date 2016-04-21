from django.shortcuts import render, render_to_response 
from django.http import Http404
#from .models import main
# Create your views here.
def main(request):
    return render(request, 'Templates/main.html', {})

