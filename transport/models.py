from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PLACE = (
    ("pkt", "Punkt Pobrań"),
    ("lab", "Laboratorium"),
    ("inny", "Inny obiekt")
)

HOURS = (
    ("6", "6.00-7.00"),
    ("7", "7.00-8.00"),
    ("8", "8.00-9.00"),
    ("9", "9.00-10.00"),
    ("10", "10.00-11.00"),
    ("11", "11.00-12.00"),
    ("12", "12.00-13.00"),
    ("inna", "Inna")
)

DAY = (
    ("pon", "Poniedziałek"),
    ("wt", "Wtorek"),
    ("śr", "Środa"),
    ("czw", "Czwartek"),
    ("pt", "Piątek"),
    ("sb", "Sobota"),
)

ROLE = (
    ("mng", "Kierownik"),
    ("drv", "Kierowca"),
)

class Sample(models.Model):
    barcode = models.IntegerField(verbose_name="Kod próbki")
    sampling_place = models.ForeignKey('Location', on_delete=models.CASCADE, verbose_name="Miejsce pobrania")
    delivery_place = models.ForeignKey('Location', on_delete=models.CASCADE, related_name="sample_delivery", verbose_name="Miejsce dostawy")
    sampling_date = models.TimeField(auto_now=True, verbose_name="Data pobrania")
    delivery_date = models.TimeField(auto_now=True, verbose_name="Data dostawy")
    in_delivery = models.BooleanField(verbose_name="W dostawie")
    drivers = models.ForeignKey('Courier', on_delete=models.CASCADE)

class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name="Marka")
    model = models.CharField(max_length=50, verbose_name="Model")
    tech_review = models.DateField(verbose_name="Przegląd techniczny")
    fridge = models.BooleanField(verbose_name="Czy jest lodówka?")
    couriers = models.ForeignKey('Courier', on_delete=models.CASCADE)
    
class Courier(models.Model):
    courier_id = models.CharField(max_length=50, verbose_name="Identyfikator")
    name = models.CharField(max_length=50, verbose_name="Imię")
    surname = models.CharField(max_length=50, verbose_name="Nazwisko")
    
class Location(models.Model):
    address = models.CharField(max_length=50, verbose_name="Adres")
    place = models.CharField(choices=PLACE, max_length=20, verbose_name="Obiekt")
    pickup_time = models.CharField(choices=HOURS,max_length=20, verbose_name="Godziny pracy")
    pickup_day = models.CharField(choices=DAY,max_length=20, verbose_name="Dni pracy")
    
class Worker(models.Model):
    role = models.CharField(choices=ROLE, max_length=20, verbose_name="Pełniona funkcja")
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
