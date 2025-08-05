from django.contrib import admin
from .models import User, Kakeibo, Budget, Subscription, Category

admin.site.register(User)
admin.site.register(Kakeibo)
admin.site.register(Budget)
admin.site.register(Subscription)
admin.site.register(Category)