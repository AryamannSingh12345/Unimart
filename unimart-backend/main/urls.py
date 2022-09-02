from django.urls import path
from unimart import settings
from . import views

urlpatterns = [
	path("home/", views.index, name='index'),
	path("", views.home, name='home'),
	path("contact-us/", views.contact_us, name='contact_us'),
	path("userpage/", views.userdetail, name='userdetail'),
	path("buyer/", views.buyer, name='buyer'),
	path("seller/", views.seller, name='seller'),
	path("seller/create-post/", views.cseller, name='cseller'),
	path("buyer/create-post/", views.cbuyer, name='cbuyer'),
    path("buyer/search/", views.buyer_search, name='buyer_search'),
    path("seller/search/", views.seller_search, name='seller_search'),
    path("buyer/my-posts/", views.my_buyer_posts, name='my_buyer_posts'),
    path("seller/my-posts/", views.my_seller_posts, name='my_seller_posts'),
]

