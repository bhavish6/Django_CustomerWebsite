from django.http import HttpResponse
from django.shortcuts import redirect
#decorators are used in python when youre for eg importing a fucnt and you dont want to change anything there
#so you can pass that funct as a parameter here and make changes here and return it again
#the inner or the wrapper funct must take he same no. of arguments as the og funct is taking
def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)

    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):                       #we are passing home as the view _func here
        def wrapper_func(request,*args,**kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:                                #if the user is in allowed groups ,hell be redirected to home as hes allowed

                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('You are not authorised to view this page')

        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'Userss':
            return redirect('userpage')

        if group == 'Adminn':
            return view_func(request,*args,**kwargs)
    return wrapper_func