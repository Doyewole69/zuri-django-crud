from re import template
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostCreateView(CreateView):
    model = Post
    fields= ["title", "slug", "author", "body", "publish", "created", "updated"]
    success_url: reverse_lazy("blog:all")
    template_name = 'post_form.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    fields= ["title", "slug", "author", "body", "publish", "created", "updated"]
    success_url: reverse_lazy("blog:all")
    template_name = 'base.html'

class PostDeleteView(DeleteView):
    model = Post
    fields= ["title", "slug", "author", "body", "publish", "created", "updated"]
    success_url: reverse_lazy("blog:all")
    template_name = 'post_confirm_delete.html'

