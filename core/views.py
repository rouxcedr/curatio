from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from .decorators import allowed_users
from .models import *


# Create your views here.
def home(request):
    context = {}
    return render(request, 'core/home.html', context)


def loginPage(request):
    context = {}
    return render(request, 'core/login.html', context)

def loginUser(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if username == password:
            print("RESET")
            login(request, user)
            return redirect('password_reset')
        elif user is not None:
            login(request, user)
            return redirect('eaubelix')
        else:
            return redirect('home')

def not_subscribed(request):
    return render(request, 'core/not_subscribed.html')

@login_required
def passwordReset(request):
    error = False
    if request.method == 'POST':
        reset_form = PasswordChangeForm(request.user, request.POST)

        if reset_form.is_valid():
            reset_form.save()
            update_session_auth_hash(request, reset_form.user)
            return redirect('eaubelix')
        else:
            error = True

    reset_form = PasswordChangeForm(user=request.user)
    reset_form.fields["old_password"].label = "Ancien mot de passe"
    reset_form.fields["new_password1"].label = "Nouveau mot de passe"
    reset_form.fields["new_password2"].label = "Confirmer votre nouveau mot de passe"
    context = {'password_reset_form': reset_form, 'error': error, }
    return render(request, 'core/password_reset.html', context)


@login_required
def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required
@allowed_users(allowed_roles=['CLIENT'])
def operators(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            clients_operators = Operator.objects.filter(operatormore__client=request.user)
            context = {'operators': clients_operators, 'error':'Ce nom d\'utilisateur éxiste deja, essayez en un autre'}
            return render(request, 'core/operators.html', context)
        new_operator = User(username=username, type=User.Types.OPERATOR)
        new_operator.set_password(username)
        new_operator.save()

        new_operator_more = OperatorMore.objects.create(user=new_operator, client=request.user)
        new_operator_more.save()
        return redirect('operators')
    clients_operators = Operator.objects.filter(operatormore__client=request.user)
    context = {'operators': clients_operators}
    return render(request, 'core/operators.html', context)


@login_required
@allowed_users(allowed_roles=['CLIENT'])
def delete_operator(request, operator_id=None):
    object = Operator.objects.get(id=operator_id)
    object.delete()
    return redirect('operators')

