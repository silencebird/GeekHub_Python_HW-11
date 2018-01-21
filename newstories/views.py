from django.shortcuts import render
from .models import Newstories


def newstories(request):
    stories = Newstories.objects.all()
    return render(request, 'newstories/index.html', {'newstories': stories})
