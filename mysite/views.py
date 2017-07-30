from django.shortcuts import redirect


def redirect_webapp(request):
    return redirect("/webapp")