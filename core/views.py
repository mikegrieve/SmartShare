from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, render, redirect
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
        form = NewItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('/core')
    else:
        form = NewItemForm()

    return render(request, 'core/create.html', {'form': form})
    

class ItemDetail(DetailView):
    model = Item
    template_name = 'core/item_detail.html'
