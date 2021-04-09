from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
# from eauxbelix.models import BoilerData


# Create your models here.
class User(AbstractUser):
    class Types(models.TextChoices):
        ADMIN = 'ADMIN', "Admin"
        EMPLOYEE = 'EMPLOYEE', "Employé"
        CLIENT = 'CLIENT', "Client"
        OPERATOR = 'OPERATOR', "Opérateur"

    type = models.CharField('Type', max_length=50, choices=Types.choices, default=Types.OPERATOR)

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def __str__(self):
        return self.username


class AdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)


class Admin(User):
    objects = AdminManager()

    class Meta:
        proxy = True
        verbose_name_plural = "Admins"
        verbose_name = "Admin"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.ADMIN


class EmployeeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.EMPLOYEE)


class Employee(User):
    objects = EmployeeManager()

    class Meta:
        proxy = True
        verbose_name_plural = "Employees"
        verbose_name = "Employee"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.EMPLOYEE


class ClientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CLIENT)

class Client(User):
    objects = ClientManager()

    @property
    def more(self):
        return self.clientmore

    class Meta:
        proxy = True
        verbose_name_plural = "Clients"
        verbose_name = "Client"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.CLIENT

class ClientMore(models.Model):
    user = models.OneToOneField(Client, on_delete=models.CASCADE)

    class Subscriptions (models.TextChoices):
        EAUBELIX = "EAUBELIX", "Eau-Belix"
        FORMATION = "FORMATION", "Formation"

    subscription = ArrayField(
        models.CharField('Subscriptions', max_length=255, choices=Subscriptions.choices, default=None, null=True), null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "Clients Data"
        verbose_name = "Client Data"

    def __str__(self):
        return self.user.username

class OperatorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.OPERATOR)


class Operator(User):
    objects = OperatorManager()

    @property
    def more(self):
        return self.operatormore

    class Meta:
        proxy = True
        verbose_name_plural = "Operators"
        verbose_name = "Operator"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.OPERATOR

class OperatorMore(models.Model):
    user = models.OneToOneField(Operator, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='operator')

    class Meta :
        verbose_name_plural = "Operators Data"
        verbose_name = "Operator Data"

    def __str__(self):
        return self.user.username
