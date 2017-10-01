from django.shortcuts import render, redirect
from george_app.models import *


def base_page(request):
    context = {}
    return render(request, 'basepage.html', context=context)


def get_all_blog(request):
    context = {}
    context['blogs'] = blogArticle.objects.all()
    return render(request, 'allblogs.html', context=context)


def get_one_blog(request, blog_id):
    context = {}
    context['blog'] = blogArticle.objects.get(id=blog_id)
    return render(request, 'oneblog.html', context=context)


def add_blog(request):
    if request.POST:
        data = request.POST.copy()
        blogArticle.objects.create(
            title=data.get('title'),
            text=data.get('text')
        )
        return redirect('get_all')
    else:
        return render(request, 'addblog.html')


def del_blog(request, blog_id):
    blogArticle.objects.get(id=blog_id).delete()
    return redirect('get_all')


def update_blog(request, blog_id):
    if request.POST:
        b = blogArticle.objects.get(id=blog_id)
        b.title = request.POST.get('title')
        b.text = request.POST.get('text')
        b.save()
        return redirect('get_all')
    else:
        context = {}
        context['blog'] = blogArticle.objects.get(id=blog_id)
        return render(request, 'addblog.html', context=context)
