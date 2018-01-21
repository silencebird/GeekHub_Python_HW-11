from django.shortcuts import render
from .models import Jobstories


def jobstories(request):
    stories = Jobstories.objects.all()
    return render(request, 'jobstories/index.html', {'jobstories': stories})
