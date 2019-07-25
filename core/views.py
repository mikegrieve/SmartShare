from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, render, redirect

from .forms import NewItemForm, NewReviewForm
from .models import Topic, Item, Review

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
    

def itemDetail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = NewReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit = False)
            review.item = item
            review.save()
            return redirect('/core/item/{}'.format(item.id))

    form = NewReviewForm()
    context = {
        'item': item,
        'reviews': item.review_set,
        'form': form
    }

    return render(request, 'core/item_detail.html', context)
