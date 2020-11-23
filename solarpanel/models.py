from django.db import models

# Create your models here.


class Agents(models.Model):
    agent_name = models.CharField(max_length=100, default="")
    agent_username = models.CharField(max_length=100, default="")
    agent_password = models.CharField(max_length=100, default="")
    agent_address = models.CharField(max_length=100, default="")
    agent_phonenumber = models.IntegerField(default='+1717176171717')

    def __str__(self):
        return self.agent_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=30, default="")
    customer_address = models.CharField(max_length=30, default="")
    customer_phonenumber = models.IntegerField(default='+1717176171717')
    customer_Zipcode = models.IntegerField(default='+171717')
    agent = models.ForeignKey(Agents, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.customer_name
