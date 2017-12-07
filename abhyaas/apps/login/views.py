from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext,loader
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def index(request):
	return HttpResponse('welcome')

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/login/login/')	


def user_login(request):
	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		#attempt to authenticate
		user = authenticate(username=username,password=password)
		#if correct details
		if user:
			if user.is_active:
				login(request,user)
				if(user.utype == 'S'):
					return HttpResponseRedirect('/student/')
				else:
					return HttpResponseRedirect('/faculty/')
			else:
				return HttpResponse('account disabled')
		else:
			#bad login details
			return HttpResponse('invalid login details')

	else:
		#not a POST request, display login form
		if request.user.is_authenticated():
			if request.user.utype=='S':
				return HttpResponseRedirect("/student/")
			else:
				return HttpResponseRedirect("/faculty/")
		else:		
			return render_to_response('login/login.html',{},context)
