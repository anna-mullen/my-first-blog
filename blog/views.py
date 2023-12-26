from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Adding below import to get 404 error for post_detail (or could I add comma & beyond to the above import?)
from django.shortcuts import render, get_object_or_404
# Adding below import to use form in view
from .forms import PostForm
# Adding below import to redirect to the new blog post after you save it
from django.shortcuts import redirect

# view of a list of posts
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# view of a single post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# view of form to create a new post
def post_new(request):
    if request.method == "POST": # This is true if you have hit the save button on the post_edit page b/c in the html we used the POST method: <form method="POST"
        form = PostForm(request.POST) # This creates a PostForm object with the data POSTed by the user
        if form.is_valid(): # Now that you've saved the PostForm object with the user's data as "form", you can validate it (ensures that every field of PostForm in forms.py is complete or displays an error) and save the validated PostForm as "post"
            post = form.save(commit=False) # commit=False means that you won't actually save these things to post until you get the command "post.save()" after adding ALL data
            post.author = request.user
            post.published_date = timezone.now()
            post.save() # This will actually commit the changes and save all your post's completed and validated data
            return redirect('post_detail', pk=post.pk) # This redirects to your new post (post_detail view with your new post's primary key)
    else: # This is the first time you're seeing the post_edit page
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# view of editing a post (uses the same template as creating a new post)
def post_edit(request, pk): # we need to pass an extra pk parameter to pre-populate the form with the current data from the pk post in question
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # This saves the current data in the variable "form"
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post) # This pre-populates the current post data in the form
    return render(request, 'blog/post_edit.html', {'form': form})