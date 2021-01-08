from django.shortcuts import render,redirect
from posts.models import Posts,PostsForm,Category
from django.views.generic import TemplateView,ListView

# Create your views here.
def index(request):
    form= PostsForm()
    data=Posts.objects.all()
    if request.method == 'POST':
        form = PostsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'index.html',{'form':form,'rows':data})

class cbview(TemplateView):
    template_name='class_view.html'

