from django.shortcuts import render
from .models import Showstories

def showstories(request):
    stories = Showstories.objects.all()
    return render(request, 'showstories/index.html', {'showstories': stories})
