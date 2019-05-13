from django.shortcuts import render, get_object_or_404
from .models import Forums

# Create your views here.

def allforums(request):
    forum = Forums.objects
    return render(request, 'forums/allforums.html', {"forums":forum})

def detail(request, blog_id):
    detailforum = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'forums/detailforum.html', {'forums':detailforum})