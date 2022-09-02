from django.contrib import admin
from .models import seller_post, buyer_post, feedback

# admin.site.register(user_details)
admin.site.register(seller_post)
admin.site.register(buyer_post)
admin.site.register(feedback)
