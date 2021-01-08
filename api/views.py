from django.http import HttpResponse
from django.core.serializers import  serialize
from posts.models import Posts

# Create your views here.
def users(request,pk=None):
    if pk is None:
        posts= Posts.objects.all()
    else:
        posts= Posts.objects.filter(pk=pk)



    posts=serialize('json',posts)
    return HttpResponse(posts,content_type='text/json')