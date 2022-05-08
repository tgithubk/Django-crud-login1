from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import Comment
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .forms import CommentForm,SignupForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout


def signupView(request):
    form = SignupForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            return HttpResponseRedirect('line/userregistrationdone.html')
        
        else:
            form = SignUpForm()
            
            return render(request, 'signup.html', {'form': form})
    template = loader.get_template('line/signup.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

def userregistrationdoneView(request):
    #template = loader.get_template('line/userregistrationdone.html')
    #context = {'user': user}
    
     #パスワードが保存されない
    u = User.objects.create_user(username = request.POST['username'],email='',password = request.POST['password'])
    u.save()
    return HttpResponse('登録完了')
       
#def logout(request):
    #logout(request)
    #return HttpResponseRedirect('registration/logout.html')
    
def LoginView(request):
    form = LoginForm(request.POST)
    
    if request.method == 'POST':
        u= request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
    
        if request.user.is_authenticated:
            login(request, user)
            return HttpResponseRedirect('line/index.html')
        
    else: #これが機能しない
        #template = loader.get_template('registration/login_error.html')
        #context = {'form': form}
        #return HttpResponse(template.render(context, request))
        return HttpResponseRedirect('registration/login_error.html')
        
#def success(request):
        #username = "username"
        #template = loader.get_template('line/success.html')
        #context = {'username': username}
        #return HttpResponse(template.render(context, request))
        
def login_error(request):
        username = "username"
        template = loader.get_template('line/login_error.html')
        context = {'username': username}
        return HttpResponse(template.render(context, request))

@login_required        
def index(request):
    if request.method == 'POST':

        form = CommentForm(request.POST)
        if form.is_valid():

            c = Comment(comment = request.POST['comment'])
            c.save()
            return HttpResponseRedirect('/line')
    
    comment_list = Comment.objects.all()
    template = loader.get_template('line/index.html')
    context = {'comment_list': comment_list}
    return HttpResponse(template.render(context, request))
    
def deleteView(request, id):
    c = get_object_or_404(Comment, pk=id)
    c.delete()
    
    return HttpResponseRedirect('/line')
    
def detailView(request, id):
    try:
        comment = Comment.objects.get(pk=id)
    except Comment.DoesNotExist:
        raise Http404("Comment does not exist")
    return render(request, 'line/detail.html', {'comment': comment})
    
def updateView(request, id):
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():

            change_data = Comment(comment = request.POST['comment'], pk=id)
            change_data.save()
            return HttpResponseRedirect('/line')

    return HttpResponseRedirect('/line')
    
