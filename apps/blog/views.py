from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.users.forms import LoginForm
from apps.blog.models import Article, Comment
from apps.blog.forms import CommentForm


def blog(request):
    login_form = LoginForm()
    if request.user.is_authenticated():
        articles = Article.objects.filter(published=True, corp=False).order_by("-created")
    else:
        articles = Article.objects.filter(published=True, public=True, corp=False).order_by("-created")
    
    #pagination
    paginator = Paginator(articles, 10, request=request)
    page = request.GET.get('page', 1)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    
    return render(request, "blog/blog.html", {"articles": articles, "login_form": login_form})
    

#show article with comments
def blog_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    form = CommentForm(request.POST or None)
    
    if request.POST and form.is_valid():
        print request.POST
    
    comments = Comment.objects.filter(reply_to=None)
    return render(request, "blog/article.html", {"form": form, "article": article, "comments": comments})
