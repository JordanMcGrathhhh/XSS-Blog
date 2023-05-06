from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import AnonymousUser

from .models import Post, Comment

# Create your views here.


class Index(View):

    template_name = 'home/index.html'
    context = {}

    def get(self, request):

        posts = Post.objects.all()

        self.context['posts'] = posts

        return render(request, template_name=self.template_name, context=self.context)


class ReadPost(View):

    template_name = 'home/read_post.html'
    context = {}

    def get(self, request, post_id):

        post = Post.objects.get(id=post_id)
        comments = Comment.objects.all().filter(post=post)

        self.context['post'] = post
        self.context['comments'] = comments

        return render(request, template_name=self.template_name, context=self.context)


class AddComment(View):

    def post(self, request):

        post = Post.objects.get(id=request.POST['post-id'])

        if request.user.is_authenticated:

            comment = Comment(
                post=post,
                author=request.user,
                content=request.POST['comment-textarea']
            )

        else:

            comment = Comment(
                post=post,
                content=request.POST['comment-textarea']
            )

        comment.save()

        return redirect('/posts/' + str(post.id))
