from django.urls import path, include
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('<int:blog_id>/', views.detail, name='blog_detail'),
    path('category/<int:category_id>/', views.category, name='blog_category'),
    path('archives/<int:year>/<int:month>', views.archives, name='blog_archives'),
    path('tag/<int:tag_id>/', views.tag, name='blog_tag'),
    path('search/', views.search, name='blog_search'),
    path('reply/<int:comment_id>/', views.reply, name='comment_reply'),
    # path('?P<blog_id>[0-9]+', views.detail, name='blog_detail'),
]