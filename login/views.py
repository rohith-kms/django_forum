from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.

# Note the is_authenticated condition. This can be used in all views to censor content for anonymous users. We can use this to hide specific information on the website by rendering different templates based on the log in status.


# Authentication can be checked within the template (as in the homepage - check out index.html for more details) or in the views (check out hidden_link view below)


def login_view(request):

	# Ask for login credentials

	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)

	# Check if user exists in the database of users
	if user is not None:

		# Login if user exists
		login(request, user)

	else:

		messages.error(request,'Invalid login credentials. Please try again.')

	# Redirect to homepage
	response = redirect('/')
	return response


def logout_view(request):

	logout(request)
	# Redirect to homepage
	response = redirect('/')
	return response

def login_page(request):

    return render(request,'login/login_page.html')
