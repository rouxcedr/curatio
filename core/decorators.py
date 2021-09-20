from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):

    def decorator(view_func):

        def wrapper_func(request, *args, **kwargs):

            if request.user.type == "CLIENT":
                if request.user.type in allowed_roles or \
                        len(list(set(request.user.clientmore.subscription) - set(allowed_roles))) \
                        < len(request.user.clientmore.subscription):
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('not_subscribed')

            if request.user.type == "OPERATOR":
                if len(list(set(request.user.operatormore.client.clientmore.subscription) - set(allowed_roles))) < len(
                        request.user.operatormore.client.clientmore.subscription):
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('not_subscribed')

            if request.user.type in allowed_roles or request.user.type == "ADMIN":
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home')

        return wrapper_func

    return decorator


