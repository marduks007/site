from django.shortcuts import render

def blog(request):

    return render(request,'blog/blog.html')

def blog_single(request):

    return render(request,'blog/blog_single.html')
