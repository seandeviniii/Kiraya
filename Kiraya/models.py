from django.db import models

# Create your models here.
class Customer(models.Model):
    """docstring for Customer."""
    
    def __init__(self, arg):
        super(Customer, self).__init__()
        self.arg = arg
