from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post, Location, Category

post_list = list(Post.objects.values(
'id', 'title', 'text', 'location', 'category'))

for post in post_list:
    location_id = post['location']
    category_id = post['category']
    location = Location.objects.get(pk=location_id)
    category = Category.objects.get(pk=category_id)
    post['location'], post['category'] = location, category


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
    template = 'blog/category.html'
    category = get_object_or_404(Category, pk=category_slug)
    context = {'category': category}
    return render(request, template, context)
