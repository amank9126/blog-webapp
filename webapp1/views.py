from django.shortcuts import render , get_object_or_404
from .models import post
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView


# Create your views here.



def home(request):
    context={
    'posts': post.objects.all()
    }
    return render(request,'webapp1/home.html', context)

class postlistview(ListView):
    model = post
    template_name = 'webapp1/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class userpostlistview(ListView):
    model = post
    template_name = 'webapp1/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3
    def get_queryset(self):
        user= get_object_or_404(User, username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date_posted')

class postdetailview(DetailView):
    model = post

class postcreateview(LoginRequiredMixin ,CreateView):
    model = post
    fields = ['title' , 'query']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class postupdateview(LoginRequiredMixin , UserPassesTestMixin ,UpdateView):
    model = post
    fields = ['title' , 'query' , 'img']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class postdeleteview(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request,'webapp1/about.html', {'title': about})
