from django.shortcuts import render, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from agency.utils import get_seo_context
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *

#Blog views
class BlogListView(ListView):
    template_name='blog/blog_list.html'
    model=Post
    context_object_name='blogs'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Post.objects.filter(status='published')
        
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_posts'] = Post.objects.filter(status='published', is_featured=True)[:3]
        context.update(get_seo_context('blog'))
    
        # Get all published posts, excluding featured
        published = Post.objects.filter(status='published', is_featured=False).order_by('-published_at')
        # Skip the most recent (first) post
        context['latest_posts'] = published[0:3]  # Next two posts, not featured
        return context


#Blog Detail View  
class BlogDetailView(DetailView):
    model=Post
    template_name='blog/blog_detail.html'
    
    
    
    def get_queryset(self):
        return Post.objects.filter(status='published')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_posts'] = Post.objects.filter(status='published', is_featured=True)[:3]
        return context

#Blog Create View     
class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name="blog/blog_create.html"
    model=Post
    form_class=BlogForm
    success_url = reverse_lazy ("blogs" )
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user  # ✅ Set author here
        response = super().form_valid(form)
        messages.success(self.request, "Blog added successfully.")
        return response

#Blog Update View     
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model=Post
    form_class=BlogForm
    template_name="blog/blog_edit.html"
    success_url=reverse_lazy("blogs")
    

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Blog updated successfully.")
        return response

#Blog Delete View     
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/blog_delete.html"
    success_url= reverse_lazy("blogs")

