from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.BigIntegerField(unique=True, null=False, blank=False)
    address = models.TextField(null=False, blank=False)


    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    # def __str__(self):
    #     return str(self.user.username)



class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/', null=False, blank=False)
    rating = models.PositiveSmallIntegerField(null=True, blank=True, default=1)
    mobile = models.BigIntegerField(unique=True, null=False, blank=False)
    pincode = models.CharField(max_length=6, null=False, blank=False)
    address = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'

    def __str__(self):
        return self.user.username



class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name






class Profession(models.Model):
    worker = models.OneToOneField(Worker, on_delete=models.CASCADE, null=False, blank=False)
    service = models.ManyToManyField(Service)

    class Meta:
        verbose_name = 'WorkerService'
        verbose_name_plural = 'WorkerServices'

    def __str__(self):
        return self.worker.user.username





class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=False, blank=False)
    booing_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    accepted = models.BooleanField(default=False)
    acceptance_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    # def __str__(self):
    #     return str(self.customer.user.username)






class Review(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=False, blank=False)
    rating = models.PositiveSmallIntegerField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    feedback = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'



