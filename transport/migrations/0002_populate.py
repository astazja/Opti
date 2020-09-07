from django.db import migrations
from transport.models import Sample, Car, Courier, Location, Worker

def populate(apps, schema_editor):
    Car.objects.create(brand='Alfa Romeo', model='MiTo', tech_review='2020-8-2', fridge=True, couriers_id=1)
    Car.objects.create(brand='Alfa Romeo', model='Giulietta', tech_review='2021-9-12', fridge=True, couriers_id=2)
    Car.objects.create(brand='Alfa Romeo', model='GT', tech_review='2021-7-9', fridge=False, couriers_id=3)
    Car.objects.create(brand='Audi', model='TT', tech_review='2020-10-15', fridge=True, couriers_id=4)
    Car.objects.create(brand='Audi', model='S8', tech_review='2021-1-2', fridge=True, couriers_id=5)
    Car.objects.create(brand='Audi', model='S5', tech_review='2021-3-5', fridge=False, couriers_id=6)
    Car.objects.create(brand='BMW', model='X6', tech_review='2020-7-3', fridge=True, couriers_id=7)
    Car.objects.create(brand='BMW', model='X3', tech_review='2021-2-18', fridge=True, couriers_id=8)
    Car.objects.create(brand='BMW', model='X5', tech_review='2021-4-23', fridge=False, couriers_id=9)
    Car.objects.create(brand='Ford', model='Puma', tech_review='2020-7-22', fridge=True, couriers_id=10)
    Car.objects.create(brand='Ford', model='Kuga', tech_review='2021-5-10', fridge=True, couriers_id=11)
    Car.objects.create(brand='Ford', model='Fiesta', tech_review='2020-7-29', fridge=False, couriers_id=12)

    Courier.objects.create(courier_id='pierwszy', name='Tomek', surname='Szybki')
    Courier.objects.create(courier_id='drugi', name='Iwona', surname='Szybka')
    Courier.objects.create(courier_id='trzeci', name='Sławek', surname='Wolny')
    Courier.objects.create(courier_id='czwarty', name='Krzyś', surname='Szybowiec')
    Courier.objects.create(courier_id='piąty', name='Bożena', surname='Szybkościowa')
    Courier.objects.create(courier_id='szósty', name='Irena', surname='Szmonowa')
    Courier.objects.create(courier_id='siódmy', name='Klaudia', surname='Kot')
    Courier.objects.create(courier_id='ósmy', name='Teresa', surname='Płot')
    Courier.objects.create(courier_id='dziewiąty', name='Monika', surname='Smok')
    Courier.objects.create(courier_id='dziesiąty', name='Sylwia', surname='Dama')
    Courier.objects.create(courier_id='jedenasty', name='Tomek', surname='Dwa')
    Courier.objects.create(courier_id='dwunasty', name='Błażej', surname='Dwulatek')

    Location.objects.create(address='Pierwsza 1/1', place='pkt', pickup_time="6", pickup_day="pon")
    Location.objects.create(address='Druga 2', place='pkt', pickup_time="7", pickup_day="wt")
    Location.objects.create(address='Trzecia 3/1', place='pkt', pickup_time="8", pickup_day="śr")
    Location.objects.create(address='Czwarta 4', place='inny', pickup_time="9", pickup_day="czw")
    Location.objects.create(address='Piąta 1/5', place='inny', pickup_time="10", pickup_day="pt")
    Location.objects.create(address='Labo 1', place='lab', pickup_time="11", pickup_day="sb")
    Location.objects.create(address='Labo 2', place='lab', pickup_time="12", pickup_day="pon")
    Location.objects.create(address='Labo 3', place='lab', pickup_time="13", pickup_day="wt")
    Location.objects.create(address='Labo 4', place='lab', pickup_time="7", pickup_day="śr")
    Location.objects.create(address='Labo 5', place='lab', pickup_time="9", pickup_day="czw")

    Worker.objects.create(role="mng", car_id=1)
    Worker.objects.create(role="drv", car_id=2)

    Sample.objects.create(barcode=1, sampling_place_id=1, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=2, sampling_place_id=2, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=4, sampling_place_id=4, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=5, sampling_place_id=5, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=6, sampling_place_id=6, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=7, sampling_place_id=7, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=8, sampling_place_id=8, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=9, sampling_place_id=9, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=10, sampling_place_id=10, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=11, sampling_place_id=1, delivery_place_id=2, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=12, sampling_place_id=2, delivery_place_id=2, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=13, sampling_place_id=3, delivery_place_id=2, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=14, sampling_place_id=4, delivery_place_id=2, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=15, sampling_place_id=5, delivery_place_id=2, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=16, sampling_place_id=6, delivery_place_id=2, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=17, sampling_place_id=7, delivery_place_id=2, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=18, sampling_place_id=8, delivery_place_id=2, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=19, sampling_place_id=9, delivery_place_id=2, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=20, sampling_place_id=10, delivery_place_id=2, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=21, sampling_place_id=1, delivery_place_id=3, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=22, sampling_place_id=2, delivery_place_id=3, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=23, sampling_place_id=3, delivery_place_id=3, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=24, sampling_place_id=4, delivery_place_id=3, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=25, sampling_place_id=5, delivery_place_id=3, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=26, sampling_place_id=6, delivery_place_id=3, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=27, sampling_place_id=7, delivery_place_id=3, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=28, sampling_place_id=8, delivery_place_id=3, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=29, sampling_place_id=9, delivery_place_id=3, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=30, sampling_place_id=10, delivery_place_id=3, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=31, sampling_place_id=1, delivery_place_id=4, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=32, sampling_place_id=2, delivery_place_id=4, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=33, sampling_place_id=3, delivery_place_id=4, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=34, sampling_place_id=4, delivery_place_id=4, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=35, sampling_place_id=5, delivery_place_id=4, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=36, sampling_place_id=6, delivery_place_id=4, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=37, sampling_place_id=7, delivery_place_id=4, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=38, sampling_place_id=8, delivery_place_id=4, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=39, sampling_place_id=9, delivery_place_id=4, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=40, sampling_place_id=10, delivery_place_id=4, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=41, sampling_place_id=1, delivery_place_id=5, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=42, sampling_place_id=2, delivery_place_id=5, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=43, sampling_place_id=3, delivery_place_id=5, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=44, sampling_place_id=4, delivery_place_id=5, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=45, sampling_place_id=5, delivery_place_id=5, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=46, sampling_place_id=6, delivery_place_id=5, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=47, sampling_place_id=7, delivery_place_id=5, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=48, sampling_place_id=8, delivery_place_id=5, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=49, sampling_place_id=9, delivery_place_id=5, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=50, sampling_place_id=10, delivery_place_id=5, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=51, sampling_place_id=1, delivery_place_id=6, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=52, sampling_place_id=2, delivery_place_id=6, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=53, sampling_place_id=3, delivery_place_id=6, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=54, sampling_place_id=4, delivery_place_id=6, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=55, sampling_place_id=5, delivery_place_id=6, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=56, sampling_place_id=6, delivery_place_id=6, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=57, sampling_place_id=7, delivery_place_id=6, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=58, sampling_place_id=8, delivery_place_id=6, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=59, sampling_place_id=9, delivery_place_id=6, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=60, sampling_place_id=10, delivery_place_id=6, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=61, sampling_place_id=1, delivery_place_id=7, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=62, sampling_place_id=2, delivery_place_id=7, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=63, sampling_place_id=3, delivery_place_id=7, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=64, sampling_place_id=4, delivery_place_id=7, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=65, sampling_place_id=5, delivery_place_id=7, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=66, sampling_place_id=6, delivery_place_id=7, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=67, sampling_place_id=7, delivery_place_id=7, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=68, sampling_place_id=8, delivery_place_id=7, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=69, sampling_place_id=9, delivery_place_id=7, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=70, sampling_place_id=10, delivery_place_id=7, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=71, sampling_place_id=1, delivery_place_id=8, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=72, sampling_place_id=2, delivery_place_id=8, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=73, sampling_place_id=3, delivery_place_id=8, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=74, sampling_place_id=4, delivery_place_id=8, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=75, sampling_place_id=5, delivery_place_id=8, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=76, sampling_place_id=6, delivery_place_id=8, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=77, sampling_place_id=7, delivery_place_id=8, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=78, sampling_place_id=8, delivery_place_id=8, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=79, sampling_place_id=9, delivery_place_id=8, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=80, sampling_place_id=10, delivery_place_id=8, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=81, sampling_place_id=1, delivery_place_id=9, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=82, sampling_place_id=2, delivery_place_id=9, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=83, sampling_place_id=3, delivery_place_id=9, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=84, sampling_place_id=4, delivery_place_id=9, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=85, sampling_place_id=5, delivery_place_id=9, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=86, sampling_place_id=6, delivery_place_id=9, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=87, sampling_place_id=7, delivery_place_id=9, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=88, sampling_place_id=8, delivery_place_id=9, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=89, sampling_place_id=9, delivery_place_id=9, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=90, sampling_place_id=10, delivery_place_id=9, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=91, sampling_place_id=1, delivery_place_id=10, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=92, sampling_place_id=2, delivery_place_id=10, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=93, sampling_place_id=3, delivery_place_id=10, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=94, sampling_place_id=4, delivery_place_id=10, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=95, sampling_place_id=5, delivery_place_id=10, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=96, sampling_place_id=6, delivery_place_id=10, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=97, sampling_place_id=7, delivery_place_id=10, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=98, sampling_place_id=8, delivery_place_id=10, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=99, sampling_place_id=9, delivery_place_id=10, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=100, sampling_place_id=10, delivery_place_id=10, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=101, sampling_place_id=1, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=102, sampling_place_id=2, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=103, sampling_place_id=3, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=104, sampling_place_id=4, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=105, sampling_place_id=5, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=106, sampling_place_id=6, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=107, sampling_place_id=7, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=108, sampling_place_id=8, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=109, sampling_place_id=9, delivery_place_id=1, in_delivery=True, drivers_id=1)
    Sample.objects.create(barcode=110, sampling_place_id=10, delivery_place_id=1, in_delivery=True, drivers_id=1)

class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(populate),
    ]