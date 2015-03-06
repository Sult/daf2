from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.users.decorators import group_required
from apps.blog.forms import ArticleForm
from apps.blog.models import Article




@group_required("moderator")
def admin(request):
    posts = {}
    posts['blog'] = Article.objects.filter(corp=False).order_by("created")[:3]
    posts['news'] = Article.objects.filter(corp=True).order_by("created")[:3]
    new_registrations = User.objects.filter(usercontrol__confirmed=False)
    inactive_dict = User.inactive_dict()
    
    return render(request, "admin/admin_overview.html", {"posts": posts, "inactive_dict": inactive_dict,
                                                        "new_registrations": new_registrations})


@group_required("moderator")
def admin_users(request):
    users = User.objects.order_by("username")
    return render(request, "admin/admin_users.html", {"users": users})



@group_required("moderator")
def user_confirm(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.usercontrol.confirmed = True
    user.usercontrol.save()
    return HttpResponseRedirect(reverse("admin_users"))


@group_required("moderator")
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse("admin_users"))


@group_required("moderator")
def blog_admin(request):
    name = "Blog"
    articles = Article.objects.filter(corp=False).order_by("-modified")
    return render(request, "admin/article_admin.html", {"articles": articles, "name": name})



@group_required("moderator")
def news_admin(request):
    name = "News"
    articles = Article.objects.filter(corp=True).order_by("-modified")
    return render(request, "admin/article_admin.html", {"articles": articles, "name": name})



#create new article 
@group_required("moderator")
def blog_create(request):
    name = "Create Blog Article"
    form = ArticleForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save_new(request.user, False)
        return HttpResponseRedirect(reverse("blog_admin"))
    
    return render(request, "admin/blog_edit.html", {"form": form, "name": name})
    
    
#create new article 
@group_required("moderator")
def news_create(request):
    name = "Create News Article"
    form = ArticleForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save_new(request.user, True)
        return HttpResponseRedirect(reverse("news_admin"))
    
    return render(request, "admin/blog_edit.html", {"form": form, "name": name})
    


@group_required("moderator")
def blog_edit(request, slug):
    article = get_object_or_404(Article, slug=slug)
    name = "Edit Blog Article"
    form = ArticleForm(request.POST or None, instance=article)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("blog_admin"))
    return render(request, "admin/blog_edit.html", {"form": form, "name": name})



@group_required("moderator")
def news_edit(request, slug):
    article = get_object_or_404(Article, slug=slug)
    name = "Edit News Article"
    form = ArticleForm(request.POST or None, instance=article)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("news_admin"))
        
    print name
    return render(request, "admin/blog_edit.html", {"form": form, "name": name})



@group_required("moderator")
def blog_preview(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "admin/blog_preview.html", {"article": article})



@group_required("moderator")
def blog_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return HttpResponseRedirect(reverse("blog_admin"))
    



