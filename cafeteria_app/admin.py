from django.contrib import admin
from .models import Student, Product, Transaction

admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Transaction)