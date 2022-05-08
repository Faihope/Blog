from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout 
from django.urls import reverse

from Blog.forms import ContactForm, PostForm,CreateUserForm,UserCreationForm
from .models import Post

# Create your views here.

def Index(request):
    posts = Post.objects.all()
    context ={'posts':posts}

    return render(request,'index.html',context)

def newPosts(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request,'Post created successfully.')
            return render(request,'newposts.html',{'form':form})
        else:
            messages.error(request,'Invalid submission!')
            # messages.error(form.error)
    else:
        form = PostForm()
    return render(request,'newposts.html',{'form':form})

def postDetail(request,pk):
    post = Post.objects.get(pk=pk)
    context = {'post':post}

    return render(request,'post-detail.html',context)

def About(request):
    return render(request,'about.html')

def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Post created successfully.')
            return render(request,'success.html',{'form':PostForm(request.GET)})
        else:
            messages.errors(request,'Invalid submission')
            messages.errors(form.errors)
    else:
        form = ContactForm()
    form = ContactForm()
    context = {'form':form}

    return render(request,'contact.html',context)

def registeruser(request):
    title = 'Register - awwards'
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!. Check out our Email later :)')

            return redirect('login')
    else:
        form = CreateUserForm
    context = {
            'title':title,
            'form':form,
                        }
    return render(request, 'registration/register.html', context)

def loginpage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username or password is incorrect')

		context = {}
		return render(request, 'registration/login.html', context)



def logout(request):
    
    return redirect(reverse('login'))