from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post, Category


def index(request):
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    ).order_by('-pub_date')[:5]

    template = 'blog/index.html'
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        pk=id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )
    template = 'blog/detail.html'
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category,
                                 slug=category_slug, is_published=True)
    post_list = category.post_set.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    )

    template = 'blog/category.html'
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
