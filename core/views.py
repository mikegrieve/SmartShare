from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import Http404

from .models import Topic

def index(request):
    topic_list = Topic.objects.all()
    context = {
        'topic_list': topic_list,
    }
    return render(request, 'core/index.html', context)

def detail(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        raise Http404("Topic does not exist")
    return render(request, 'core/detail.html', {'topic': topic}) 

def create(request):
    if request.method == 'GET':
        return render(request, 'core/create.html', {})
    elif request.method == 'POST':
        print(request['POST'])
        return HttpResponseRedirect('/core')

