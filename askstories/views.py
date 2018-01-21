from django.shortcuts import render
from .models import Askstories

def askstories(request):
    stories = Askstories.objects.all()
    return render(request, 'askstories/index.html', {'stories': stories})
