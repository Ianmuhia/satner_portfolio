from django.shortcuts import render
from django.contrib.auth import login,logout

# Create your views here.
def Login(request):
    return render(request, 'accounts/login.html')

# #register logic
# def register(request):
#     if request.method == 'POST':
#         #get for, values
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password =request.POST['password']
#         password2 = request.POST['passsword2']
#
#         #check if passwords match
#

