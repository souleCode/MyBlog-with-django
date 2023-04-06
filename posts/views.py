from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator


#Un decorateur pour mettre que si l'utilisateur n'est pas connexte il n'pas la pas inedex.html

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    posts=Post.objects.order_by('-id').all()
    paginator=Paginator(posts,3)
    
    page_number= request.GET.get('page')
    page_object = paginator.get_page(page_number)
    
    posts_number=Post.objects.count()
    message=f'{posts_number} posts: '
    
    if posts_number ==1:
        message=f'{posts_number} post: '
    
    context={
        'posts':page_object,
    
        'message':message
        
    }
    return render(request,'posts/index.html',context)

@login_required
def show(request, id):
    post=Post.objects.get(id=id)
    context={
        
        'post':post,
    }
    
    return render(request,'posts/show.html',context)

@login_required
def news_post(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)  #request.FILES permet de faire une requete de type get sur les fichiers
                                                    #sans elle on pourra pas soumettre notre formulaire de creation avec une image.        
        if form.is_valid():
            form=form.save(commit=False) # commmit est par defaut a true,si on a le met a false on va d'abord enregistrer 
                                          #le formulaire dans une variable avant de l'enregistrer dans la base de donnee.           
            form.user= request.user     #resquest.user permet de renvoyer l'utilsateur connectee.
            form.save()
            return redirect('posts:home')
    else:
        form=PostForm()        
    context={
        'form':form,
    }
    return render(request,'posts/new_post.html',context)

def update_post(request,id):
    post=Post.objects.get(id=id)
    if post.user == request.user :
        if request.method=='POST':
           form=PostForm(request.POST,request.FILES,instance=post)
           if form.is_valid():
             form.save()              
             return redirect('posts:home')
        else:
         form=PostForm(instance=post)
    else:
        raise Http404    
            
        
    context={
        'form':form,
        'post':post,
    }
    return render(request,'posts/update.html',context)


def delete_post(request,id):
    post=Post.objects.get(id=id)
    if post.user == request.user:
      post.delete()
    # return render(request,'posts/delete_post')
      return redirect('posts:home')
    else:
        raise Http404 # raise permet d'nvoyer une erreur en ptyhon. Toute cette condtion if permet de renforcer la securite de la permission.
    
@login_required    
def search_posts(request):
    search=request.GET.get('search') # le nom defini dans le formulaire pour search sera passe en parametre de get().
    posts= Post.objects.filter(Q(title__icontains= search) |
                               Q(content__icontains= search) |
                               Q(image__icontains= search))
    
    posts_number=posts.count()
    message = f'{posts_number} Resulats: '
    
    if posts_number ==1:
        message = f'{posts_number} Result: '
    context={
        'message':message,
        'posts':posts
    }
    return render(request,'posts/search_posts.html',context)
        