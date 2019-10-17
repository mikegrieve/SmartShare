from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, NewItemForm, NewReviewForm
from .models import Topic, Item, Review

def index(request):
    topic_list = Topic.objects.all()
    item_list = Item.objects.all()
    context = {
        'topic_list': topic_list,
        'item_list': item_list,
    }
    return render(request, 'core/index.html', context)

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'core/signup.html'

class TopicDetail(DetailView):
    model = Topic
    template_name = 'core/topic_detail.html'

def itemCreate(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('/core/{}'.format(item.id))
    else:
        form = NewItemForm()

    return render(request, 'core/item_create.html', {'form': form})
    

def itemDetail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item,
        'reviews': item.review_set
    }
    return render(request, 'core/item_detail.html', context)

@login_required
def itemReview(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = NewReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit = False)
            review.user = request.user
            review.item = item
            review.save()
            return redirect('/core/item/{}'.format(item.id))

    form = NewReviewForm()
    context = {
        'item': item,
        'form': form
    }
    return render(request, 'core/item_review.html', context)