from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

# Create your views here.
from django import forms
from django.shortcuts import render, redirect

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    print (queryset)


def user_management_dashboard(request):
    return render(request, 'dashboard.html')

def user_details(request):
    # Fetch user data from the database
    # Implement logic to filter and search if necessary
    users = User.objects.all()
    return JsonResponse({'users': user_list})

class AccountCreationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

def account_creation(request):
    # Handle dummy request for account creation form
    if request.method == 'POST':
         # Instantiate the form with the submitted data
        form = AccountCreationForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Process form data and create a new account
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

         # Create a new user 
            new_user = User.objects.create_user(username=username, email=email, password=password)
            return redirect('success_page')
    else:
        # If the request method is not 'POST', create a new instance of the form
        form = AccountCreationForm()
    return render(request, 'account_creation.html', {'form': form})
