from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views

from Miniature_market.main.models import BlogPost


class BlogPageView(LoginRequiredMixin, views.ListView):
    model = BlogPost
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 3



class BlogDetailsPageView(views.DetailView):
    model = BlogPost
    template_name = 'blog/blog-details.html'
    context_object_name = 'post'

