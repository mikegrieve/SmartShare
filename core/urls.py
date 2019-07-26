from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<int:pk>/', views.TopicDetail.as_view(), name='topic_detail'),
    path('item/', views.itemCreate, name='item_create'),
    path('item/<int:item_id>/', views.itemDetail, name='item_detail'),
    path('item/<int:item_id>/review/', views.itemReview, name='item_review')
]