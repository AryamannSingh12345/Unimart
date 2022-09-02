from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import seller_post, buyer_post, feedback
from main import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
	if request.user.is_authenticated:
		return render(request, "homepage2.html")
	return render(request, "homepage.html")

def home(request):
	return redirect("home/")

def contact_us(request):
    if request.method=="POST":
        femail = request.POST.get("email")
        fname = request.POST.get("name")
        fmessage = request.POST.get("message")

        feedback.objects.create(email_id=femail, name=fname, message=fmessage)
    return render(request, "contactus.html")


def seller_search(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            pname = request.POST['product_name']
            buyer_posts = buyer_post.objects.filter(product_name=pname)
            return render(request, 'buyerpostdisplay.html', {'buyer_posts': buyer_posts})
        return render(request, "sellersearchpage.html")
    return render(request, "notloggedin.html")

def my_buyer_posts(request):
    if request.user.is_authenticated:
        user = request.user
        buyer_posts = buyer_post.objects.filter(user=user)
        return render(request, 'mybuyerposts.html', {'buyer_posts': buyer_posts})
    return render(request, "notloggedin.html")

def my_seller_posts(request):
    if request.user.is_authenticated:
        user = request.user
        seller_posts = seller_post.objects.filter(user=user)
        return render(request, 'mysellerposts.html', {'seller_posts': seller_posts})
    return render(request, "notloggedin.html")

def buyer_search(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            pname = request.POST['product_name']
            seller_posts = seller_post.objects.filter(product_name=pname)
            return render(request, 'productpage.html', {'seller_posts': seller_posts})
        return render(request, "buyersearchpage.html")
    return render(request, "notloggedin.html")

def cseller(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            new_img = models.seller_post(
                user= request.user,
                product_name=request.POST.get("product_name"),
                price=request.POST.get("price"),
                exchange_items=request.POST.get("ex_items"),
                product_description=request.POST.get("details"),
                preferred_location=request.POST.get("location"),
                preferred_contact=request.POST.get("contact"),
                img=request.FILES.get("image"),
                image_name=request.FILES.get("image").name,
            )
            new_img.save()

            return redirect("/seller/create-post/")

        return render(request, 'createsellerpost.html')
    return render(request, "notloggedin.html")

def cbuyer(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'createbuyerpost.html')

        user = request.user
        bproduct = request.POST.get("product_name")
        bprice = request.POST.get("budget")
        bdetails = request.POST.get("details")
        blocation = request.POST.get("location")
        bcontact = request.POST.get("contact")

        buyer_post.objects.create(user=user, product_name=bproduct, budget_range=bprice, preference_details=bdetails,
                                  preferred_location=blocation, preferred_contact=bcontact)

        return redirect("/buyer/create-post/")
    return render(request, "notloggedin.html")

def dfeedback(request):
    if request.method == "GET":
        return render(request, '')

    femail = request.POST.get("")
    fname = request.POST.get("")
    fmessage = request.POST.get("")

    feedback.objects.create(email_id=femail, name=fname, message=fmessage)

def buyer(request):
    if request.user.is_authenticated:
        return render(request, "buyer_select.html")
    return render(request, "notloggedin.html")

def seller(request):
    if request.user.is_authenticated:
        return render(request, "seller_select.html")
    return render(request, "notloggedin.html")

def userdetail(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        return render(request, 'userdetail.html', {"user": user})
    return render(request, "notloggedin.html")