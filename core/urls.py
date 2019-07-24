from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.TopicDetail.as_view(), name='topic_detail'),
    path('item', views.createItem, name='create_item'),
    path('item/<int:pk>/', views.ItemDetail.as_view(), name='item_detail'),
]