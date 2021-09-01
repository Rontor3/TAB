from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Basic_travel(models.Model):
    name=models.CharField(max_length=14)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
    phone_number = models.CharField( validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    days=models.IntegerField()
    departure=models.DateField()
    origin = models.CharField(max_length=200)
    Numberoftravellers = models.IntegerField()
    proof = models.ImageField(upload_to='pics')
    abudget = models.IntegerField()
    mode_of_travel = models.CharField(max_length=100,null=True,blank=True)
    explore_route = models.CharField(max_length=100, null=True, blank=True)
    Destination_tour = models.CharField(max_length=100, null=True, blank=True)
    type_hotel = models.CharField(max_length=100, null=True, blank=True)
    location_destination = models.CharField( max_length=100, null=True, blank=True)
    Activities =models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    
class Place(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Destination_image(models.Model):
    img = models.ImageField(upload_to='desti')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.place.name
class mode_of_travel(models.Model):
    mot = models.CharField(max_length=100)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)

    def __str__(self):
        return self.place.name
class explore_route(models.Model):
    er = models.CharField(max_length=100)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.place.name
class Destination_tour(models.Model):
    dt = models.CharField(max_length=100)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.place.name
class type_hotel(models.Model):
    th = models.CharField(max_length=100)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.place.name
class location_destination(models.Model):
    ld = models.CharField(max_length=100)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.place.name
class Acti(models.Model):
    activity = models.CharField(max_length=100)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.place.name



    


    

