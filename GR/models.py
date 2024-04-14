from django.db import models

# Create your models here.

class userAccounts(models.Model):
    firstName=models.CharField(max_length=10)
    lastName=models.CharField(max_length=10)
    emailId=models.CharField(max_length=10,primary_key=True)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.firstName+" "+self.lastName


class addToCarProducts(models.Model):
    name=models.CharField(max_length=15)
    quantity=models.IntegerField()
    price=models.FloatField()
    imageName=models.CharField(max_length=30)
    user_Accounts=models.ForeignKey(userAccounts, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class userQuary(models.Model):
    name=models.CharField(max_length=20)
    emailId=models.CharField(max_length=30,primary_key=True)
    number=models.IntegerField()
    comment=models.CharField(max_length=200)

    def __str_(self):
        return self.name
    