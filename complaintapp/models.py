from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Types(models.TextChoices):
        ENGINEER = 'ENGINEER', 'ENGINEER'
        CUSTOMER = 'CUSTOMER', 'CUSTOMER'
        CAREDESK = 'CAREDESK', 'CAREDESK'


    name = models.CharField(max_length=255, blank=False, null=False)
    # what type of user are we
    usertype = models.CharField(
        choices=Types.choices,
        default=Types.CUSTOMER,
        max_length=255, 
        blank=False, 
        null=False
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class EngineerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(usertype=User.Types.ENGINEER)


class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(usertype=User.Types.CUSTOMER)


class CaredeskManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(usertype=User.Types.CAREDESK)


class Engineer(User):
    objects = EngineerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.usertype =User.Types.ENGINEER
        return super().save(*args, **kwargs)


class Customer(User):
    objects = CustomerManager()

    class Meta:
        proxy =  True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.usertype =User.Types.CUSTOMER
        return super().save(*args, **kwargs)

class Caredesk(User):
    objects = CaredeskManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.usertype =User.Types.CAREDESK
        return super().save(*args, **kwargs)

class Regions(models.Model):
    name =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "regions"
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.name


class Locations(models.Model):
    regionID = models.ForeignKey(Regions, on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "locations"
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name


class Complaints(models.Model):
    class Categories(models.TextChoices): 
        VOICE = 'VOICE', 'Voice'
        DATA = 'DATA', 'Data'
    
    details = models.CharField(max_length=150)
    category = models.CharField(
        choices=Categories.choices, 
        blank=False, 
        default=Categories.DATA, 
        max_length=100
    )
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    landmark = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "complaints"
        verbose_name = "Complaint"
        verbose_name_plural = "Complaints"

    def __str__(self):
        return self.details


class Tasks(models.Model):
    class Types(models.TextChoices):
        OPEN = 'OPEN', 'OPEN'
        PENDING = 'PENDING', 'PENDING'
        CLOSED = 'CLOSED', 'CLOSED'

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    complaint = models.ForeignKey(Complaints, on_delete=models.CASCADE, blank=False, null=False)
    status = models.CharField(
        choices=Types.choices, 
        blank=False, 
        null=False, 
        default=Types.OPEN,
        max_length=10
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tasks"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.complaint.details

class TaskActions(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    details =  models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # db_table = "taskactions"
        verbose_name = "Task Action"
        verbose_name_plural = "Task Actions"

    def __str__(self):
        return self.details
