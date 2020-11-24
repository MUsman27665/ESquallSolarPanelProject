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
    customer_response_choice = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Thinking', 'Thinking'),
    ]
    customer_name = models.CharField(max_length=300, default="")
    customer_address = models.CharField(max_length=300, default="")
    customer_phonenumber = models.CharField(max_length=15, default='+1717176171717')
    customer_Zipcode = models.IntegerField(default='+171717')
    total_kwh = models.IntegerField(default='+1717176171717', null=True, blank=True)
    previous_total_price = models.IntegerField(default='+1717176171717', null=True, blank=True)
    years_since_proposal = models.IntegerField(default='+1717176171717', null=True, blank=True)
    current_total = models.IntegerField(default='+1717176171717', null=True, blank=True)
    previous_savings = models.IntegerField(default='+1717176171717', null=True, blank=True)
    future_savings = models.IntegerField(default='+1717176171717', null=True, blank=True)
    customer_response = models.CharField(choices=customer_response_choice, max_length=200, default='Thinking')
    agent = models.ForeignKey(Agents, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.customer_name
