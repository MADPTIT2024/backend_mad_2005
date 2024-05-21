from django.db import models


class FullName(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Address(models.Model):
    noHouse = models.CharField(max_length=100)
    street = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.noHouse} {self.street}"


class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username} {self.password}"


class User(models.Model):
    fullname = models.OneToOneField("FullName", on_delete=models.CASCADE)
    address = models.OneToOneField("Address", on_delete=models.CASCADE)
    account = models.OneToOneField("Account", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fullname}"
