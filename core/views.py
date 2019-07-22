from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Topic, Item

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
    topic_list = Topic.objects.all()
    if request.method == 'GET':
        context = {
            'topic_list': topic_list,
        }
        return render(request, 'core/create.html', context)
    elif request.method == 'POST':
        try:
            selected_topic = get_object_or_404(Topic, pk=request.POST['topic'])
        except (KeyError, Topic.DoesNotExist):
            return render(request, 'core/create.html', {
                'topic_list': topic_list,
                'error_message': "Bad Post.",
            })
        else:
            Item.objects.create(name=request.POST['name'], topic=selected_topic)
            return HttpResponseRedirect('/core')
