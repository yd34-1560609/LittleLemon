from django.db import models

# Create your models here.
# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(max_length=5)
    booking_date = models.DateField()
    
    def __str__(self): 
        return self.name


# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10, decimal_places=2) 
   inventory = models.IntegerField(max_length=5)

   def __str__(self):
      return self.title