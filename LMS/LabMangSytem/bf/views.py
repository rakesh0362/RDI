from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
import pyrebase
from django.contrib import auth
from . models import HotMetal
from . forms import HMform
from django.http import HttpResponseRedirect



config = {
    'apiKey': "AIzaSyDggL9Iq4DeNGgC7FDaupDZdLKucxJ9cqc",
    'authDomain': "laboratorymanagmentsystem.firebaseapp.com",
    'databaseURL': "https://laboratorymanagmentsystem.firebaseio.com",
    'projectId': "laboratorymanagmentsystem",
    'storageBucket': "laboratorymanagmentsystem.appspot.com",
    'messagingSenderId': "203700881654"
}

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()

def signIn(request):

    return render(request, "welcome.html")

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message="invalid credentials"
        return render(request, "index.html",{"messg": message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "welcome.html", {"e": email})


def index (request):
    return render(request, "index.html")

def logout(request):
    auth.logout(request)
    return render(request, 'index.html')

def HMform (request):
    return render(request, "HMform.html")

def submitform (request):
    if request.POST:
        form = HotMetal(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')

    else:
        form = HotMetal()

    args = {}
    args['form'] = form
    return render_to_response('index.html', args)


