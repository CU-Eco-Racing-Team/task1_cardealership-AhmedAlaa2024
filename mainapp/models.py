from django.db import models

# Create your models here.
class Worker(models.Model):
    ssn = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=10, null=True) # Ignoring the MSB that equal 0, For example: 1046729145 instead of 01046729145
    is_promoted = models.BooleanField(default=False)


class Customer(models.Model):
    ssn = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50, null=False)
    phone_number = models.IntegerField(null=True) # Ignoring the MSB that equal 0, For example: 1046729145 instead of 01046729145


class Industry(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50, null=False)
    phone_number = models.IntegerField(null=True) # Ignoring the MSB that equal 0, For example: 1046729145 instead of 01046729145


class Cars(models.Model):
    plate_number = models.IntegerField(primary_key=True, unique=True, null=False)
    customer_ssn = models.ForeignKey(Customer, related_name='cars', null=False, on_delete=models.CASCADE)
    model = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False)
    industry_id = models.ForeignKey(Industry, related_name='cars', null=False, on_delete=models.CASCADE)


class Supervisor(models.Model):
    id = models.OneToOneField(Worker, related_name='supervisors', primary_key=True, unique=True, null=False, on_delete=models.CASCADE)


class Payment(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    plate_number = models.ForeignKey(Cars, related_name='payments', null=False, on_delete=models.CASCADE)
    method = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)


class Contract(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    industry_id = models.ForeignKey(Industry, related_name='contracts', null=False, on_delete=models.CASCADE)
    supervisor_id = models.ForeignKey(Supervisor, related_name='contracts', null=False, on_delete=models.CASCADE)
    cars_count = models.IntegerField(null=False)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)