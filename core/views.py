from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .forms import NewItemForm
from .models import Topic, Item

def index(request):
    topic_list = Topic.objects.all()
    context = {
        'topic_list': topic_list,
    }
    return render(request, 'core/index.html', context)

class TopicDetail(DetailView):
    model = Topic
    template_name = 'core/topic_detail.html'

def createItem(request):
    if request.method == 'POST':
        print('post')
    else:
        form = NewItemForm()
    return render(request, 'core/create.html', {'form': form})

    # topic_list = Topic.objects.all()
    # if request.method == 'GET':
    #     context = {
    #         'topic_list': topic_list,
    #     }
    #     return render(request, 'core/create.html', context)
    # elif request.method == 'POST':
    #     try:
    #         selected_topic = get_object_or_404(Topic, pk=request.POST['topic'])
    #     except (KeyError, Topic.DoesNotExist):
    #         return render(request, 'core/create.html', {
    #             'topic_list': topic_list,
    #             'error_message': "Bad Post.",
    #         })
    #     else:
    #         Item.objects.create(
    #             name=request.POST['name'], 
    #             topic=selected_topic,
    #             description=request.POST['name'],
    #             img_src=request.POST['img_src'],
    #             link=request.POST['link'],
    #             rating=request.POST['rating']
    #         )
    #         print(request.POST)
    #         return HttpResponseRedirect('/core')

class ItemDetail(DetailView):
    model = Item
    template_name = 'core/item_detail.html'
