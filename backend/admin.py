from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.


# admin.site.register(Customer)
# admin.site.register(Worker)
admin.site.register(Service)
# admin.site.register(Profession)
# admin.site.register(Booking)
# admin.site.register(Review)


admin.site.unregister(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username']
    class Meta:
        model = User


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "mobile", "address")



@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("id", "user")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "worker", "date")


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ("id", "worker")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "worker", "booking_date", "accepted", "acceptance_date")




admin.site.register(User, UserAdmin)
