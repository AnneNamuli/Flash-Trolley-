from django.shortcuts import render, redirect
from .models import Customer, Product
from .forms import RegistrationForm, SignInForm
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/signin')

    else:
        form = RegistrationForm()
    return render(request, 'flashTrolley/register.html', {'register_form': form})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_login(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = SignInForm()
    return render(request, 'flashTrolley/signin.html', {'form': form})

def home(request):
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user})
    return render_to_response('flashTrolley/index.html', context_instance=context)

def view_product(request):
    products=Product.objects.all()
    return render(request, 'flashTrolley/products.html', {'products': products})
