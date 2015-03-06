from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField


class Article(models.Model):
    """Represents a blog article"""
    
    title = models.CharField(max_length=62)
    slug = models.SlugField(unique=True, max_length=100)
    body = FroalaField()
    
    public = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    sticky = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    corp = models.BooleanField(default=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)

    
    def __unicode__(self):
        return self.title
    
    
    def show_modified(self):
        return self.modified.strftime("%B %d, %Y %H:%M")



class Comment(models.Model):
    """ Article comments """
    
    article = models.ForeignKey(Article)
    reply_to = models.ForeignKey("blog.Comment", null=True)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(User, null=True)
    
    def __unicode__(self):
        return "Comment from %s" % (self.author.username)
    
    
    
    
