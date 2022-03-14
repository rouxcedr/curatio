from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.db.models.query_utils import Q
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string

from .decorators import allowed_users
from .models import *
from .forms import NewUserForm, EmailForm

from formations.models import *

import urllib.parse
import json

# Create your views here.
def home(request):
    context = {}
    return render(request, 'core/home.html', context)


def loginPage(request):
    context = {"nbar": "login"}
    return render(request, 'core/login.html', context)


def loginUser(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('training_courses')
        else:
            messages.error(request, "Nom utilisateur et/ou mot de passe non valide(s). Veuillez réessayer.")
            return redirect('login_page')


def registerPage(request, data):
    decoded_data = str(urlsafe_base64_decode(data).decode("utf-8"))
    data_list = urllib.parse.unquote(decoded_data).split("&")
    email = data_list[0].split("=")[1]
    client = data_list[1].split("=")[1]
    type = data_list[2].split("=")[1]


    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():

            # Check if max operator is reached
            if type == "OPERATOR":
                client = User.objects.get(username=request.POST['client'])

                if client.clientmore.max_operator >= len(client.operator.all()):
                    messages.error(request, "Le nombre maximal d'opérateur a été atteint pour le compte client associé.")
                    messages.info(request, "Veuillez contacter votre superviseur afin d'augmenter le nombre d'opérateur maximal pour pouvoir vous enregistrer.")
                    return redirect('register_page', data)

            user = form.save()
            type = form.cleaned_data['type']
            # Create more info based on account type:
            if type == "CLIENT":
                subscription = request.POST['subscription']
                max_operator = request.POST['max_operator']
                company = request.POST['company']
                new_client_more = ClientMore.objects.create(user=user, subscription=subscription, max_operator=max_operator, company=company)
                new_client_more.save()

            if type == "OPERATOR":
                client = User.objects.get(username=request.POST['client'])
                new_operator_more = OperatorMore.objects.create(user=user, client=client)
                new_operator_more.save()

            login(request, user)
            return redirect("training_courses")
        else:
            errors = json.loads(form.errors.as_json())
            print(errors)
            if "username" in errors:
                messages.error(request, "Un utilisateur avec ce nom d'utilisateur existe déjà, veuillez utiliser un autre.")
            if "password2" in errors:
                messages.error(request, "Le mot de passe ne répond pas aux exigences et/ou les deux champs de mot de passe ne correspondaient pas, veuillez reesayer.")
    context = {}
    if type == "OPERATOR":
        context = {"form": NewUserForm(), "email": email, "type": type, "client":client}
    if type == "CLIENT":
        context = {"form": NewUserForm(), "email": email, "type": type, "subscription":"FORMATION"}
    return render(request, 'core/register.html', context)


def not_subscribed(request):
    return render(request, 'core/not_subscribed.html')

def forgot_username(request):
    if request.method == "POST":
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            email = email_form.cleaned_data["email"]
            associated_users = User.objects.filter(Q(email=email))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Nom d'utilistateur de Compte"
                    email_template_name = "core/forgot_username_email.txt"
                    email_content = {
                        "email": email,
                        "username": user.username ,
                    }

                    email_message = render_to_string(email_template_name, email_content)

                    try:
                        send_mail(subject, email_message, 'noreply@groupecuratio.ca', [email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("login_page")

            else:
                messages.error(request, "Aucun nom d'utilisateur est relié a cet adresse email.")

    email_form = EmailForm()
    return render(request, "core/forgot_username.html", {"email_form": email_form})

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Réinitialisation du Mot de Passe Demandée"
                    email_template_name = "core/password_reset_email.txt"
                    email_content = {
                        "email": user.email,
                        'domain': 'groupecuratio.ca',
                        'site_name': 'Groupe Curatio',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, email_content)
                    try:
                        send_mail(subject, email, 'noreply@groupecuratio.ca', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
            else:
                messages.error(request, "Cet addresse email n'est pas lié à un compte.")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="core/password_reset.html",
                  context={"password_reset_form": password_reset_form})

@login_required
def ProfilePage(request):

    try:
        if request.user.type == "OPERATOR":
            client = request.user.operatormore.client
        elif request.user.type == "CLIENT":
            client = request.user
        else:
            client = None

        client_training_course = TrainingCourse.objects.get(client=client)

    except TrainingCourse.DoesNotExist:
        client_training_course = None

    progression = int((request.user.user_formation_tracking.test_completed / len(client_training_course.training_video.all())) * 100)

    training_videos = client_training_course.training_video.order_by("video_order")
    operateur_form = EmailForm()
    clients_operators = Operator.objects.filter(operatormore__client=request.user)

    context = {
        "nbar":"profile",
        "operateur_form":operateur_form,
        'operators': clients_operators,
        "training_videos":training_videos,
        "progression": progression,
    }

    return render(request, 'core/profile.html', context)

@login_required
@allowed_users(allowed_roles=['CLIENT'])
def sendOperatorRegistrationEmail(request):
    if request.method == "POST":
        operateur_form = EmailForm(request.POST)
        if operateur_form.is_valid():
            operateur_email = operateur_form.cleaned_data["email"]

            if User.objects.filter(Q(email=operateur_email)).exists():
                messages.error(request, "Cet adresse email est deja utiliser")
                return redirect("profile_page")

            client = request.user
            url_param = urlsafe_base64_encode(force_bytes(urllib.parse.urlencode({"email":operateur_email, "client":client, "type":"OPERATOR"})))
            subject = "Création de Compte"
            email_template_name = "core/registration_email.txt"
            email_content = {
                "email": operateur_email,
                'domain': 'groupecuratio.ca',
                'site_name': 'Groupe Curatio',
                "url_param": url_param,
                'protocol': 'http',
            }

            email = render_to_string(email_template_name, email_content)
            try:
                send_mail(subject, email, 'noreply@groupecuratio.ca', [operateur_email], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("profile_page")

    return redirect("profile_page")


@login_required
def logoutUser(request):
    logout(request)
    return redirect('home')
