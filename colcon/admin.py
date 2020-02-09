from django.contrib import admin
from .models import Channel,UserDetails,Post,Profile,Comments

admin.site.register(Channel)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(UserDetails)