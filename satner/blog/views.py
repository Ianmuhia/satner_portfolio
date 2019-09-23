from blog.models import Post
from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from .forms import Comment, signupForm

from django.views.generic import DetailView, ListView, View, CreateView, UpdateView
from marketing.models import Signup


# def blog_single(request):
#     post_list = Post.objects.all()
#     paginator = Paginator(Post, 1)
#     page_request_var = 'page'
#     page = request.GET.get(page_request_var)
#     try:
#         paginated_queryset = paginator.page(page)
#     except PageNotAnInteger:
#         paginated_queryset = paginator.page(1)
#     except:
#         paginated_queryset = paginator.page(paginator.num_pages)
#
#     context = {
#         'queryset': post_list,
#         "page_request_var": page_request_var
#
#     }
#     return render(request, "blog/single-blog.html", context)


class IndexView(View):
    form = signupForm()

    def get(self, request, *args, **kwargs):
        featured = Post.objects.filter(Featured=True)
        blog = Post.objects.all()
        latest = Post.objects.order_by('-post_date')[0:3]
        context = {
            'object_list': featured,
            "blog": blog,
            'latest': latest,
            'form': self.form
        }

        return render(request, 'blog/blog.html', context)

    def post(self, request, *args, **kwargs):
        Email = request.POST.get("email")
        new_signup = Signup()
        new_signup.email = Email
        new_signup.save()
        messages.info(request, "successfully subscribed")
        return redirect("blog_index")


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__contains=query) |
            Q(categories__post__Description__contains=query)
        ).distinct(
        )
        context = {
            "queryset": queryset
        }
        return render(request, 'serch_results.html', context)


def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset


class blog_single(ListView):
    form = signupForm
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'queryset'
    paginate_by = 1


# def blog_index(request):
#
#
#     featured = Post.objects.filter(Featured=True)
#     blog = Post.objects.all()
#     latest = Post.objects.order_by("-post_date")[0:3]


#     if request.method == "POST":
#         print(request.POST)
#         Email = request.POST.get("email")
#         new_signup = Signup()
#         new_signup.email = Email
#         new_signup.save()

#     context = {
#         "posts":blog,
#         "blog": featured,
#         "latest": latest,

#             }
#     return render(request, "blog/blog.html", context)
