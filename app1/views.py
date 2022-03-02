
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout # visable pages using django login session method
from  django.contrib.auth.decorators import login_required
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def loginpage(request):
    return render(request, 'login.html')

#this function is login visable pages using login session method
@login_required(login_url='adminlogin')
def about(request):
    return render(request, 'about.html')


#this function is login visable pages using session method
# def about(request):
#     if 'uid' in request.session:
#         return render(request, 'about.html')
#     return render(request, 'login.html')


# #this function is login visable pages using session method
# def about(request):
#     if 'uid' in request.session:
#         return render(request, 'about.html')
#     return render(request, 'login.html')

#this function is login visable pages using django login session method
# def about(request):
#     if request.user.is_authenticated:
#         return render(request, 'about.html')
#     return render(request, 'login.html')



#signup page
def usercreate(request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpass=request.POST['cpassword']
        email=request.POST['email']

        if password==cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This Username Is Already Exists!!!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=username,
                    password=password,
                    email=email,
                )
                user.save()
        else:
            messages.info(request, 'Password doesnot match!!!!!')
            return redirect('signup')
        return redirect('login')
    else:
        return render(request, 'signup.html')

#login page
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # request.session['uid'] = user.id #visable pages using session method
        if user is not None:
            # login(request, user) #this function is login visable pages using django login session method
            auth.login(request, user)
            messages.info(request, f'Welcome {username}')#pass users name to welcome page
            return redirect('about')
        else:
            messages.info(request, 'invalid username and password, try again')
            return redirect('loginpage')
    else:
        return redirect('loginpage')

# logoutpage
@login_required(login_url='adminlogin') #login  session method
def adminlogout(request):
    # if request.user.is_authenticated: # visable pages using django login session method
    #request.session['uid']= '' #visable pages using session method
    auth.logout(request)
    return redirect('index')

