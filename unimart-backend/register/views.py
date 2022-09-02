from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User

def register(request):
	if request.method == "POST":
		email = request.POST.get("email")
		form = RegisterForm(request.POST)
		print(form)
		if form.is_valid(): #and ("@student.manchester.ac.uk" in email): this code allows only people with student.manchester id to access the website
			form.save()
			messages.success(request, "Registration successful." )
			return redirect("/login/")
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
			return render(request, "registerpage.html", {"message":"Password does not meet the specification or Data Fields Empty"})

	else:
		form = RegisterForm()
		return render(request, "registerpage.html", {"form":form})