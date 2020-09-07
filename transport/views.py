from django.shortcuts import render, redirect
from django.views import View

from .models import PLACE, HOURS, DAY, Sample, Car, Courier, Location, Worker
from django.core.paginator import Paginator
import datetime


# Create your views here.
class LandingPageView(View):
    def get(self, request):
        return render(request, "base.html")

class CourierView(View):
    def get(self, request):
        car = Car.objects.get(couriers_id=8)
        confirm = "Tak"
        if car.fridge == False:
            confirm = "Nie"
        context = {
            "car":car,
            "confirm":confirm
        }
        return render(request, "couriers_panel/courier.html", context)

class SampleReciveView(View):
    def get(self,request):
        locations = Location.objects.all()
        return render(request, "couriers_panel/sample_recive.html", {"locations":locations})
    def post(self, request):
        try:
            barcode = int(request.POST.get("barcode"))
            delivery_place_id = int(request.POST.get("delivery_place_id"))
            sampling_place_id = int(request.POST.get("sampling_place_id"))
        except (ValueError):
            return render(request, "couriers_panel/sample_recive.html", {'error_message': "Wypełnij poprawnie wszystkie pola."})
        else:
            if barcode == "":
                return render(request, "couriers_panel/sample_recive.html", {'error_message': "Podaj kod kreskowy próbki."})
            else:
                Sample.objects.create(barcode=barcode,
                                      delivery_place_id=delivery_place_id,
                                      sampling_place_id=sampling_place_id,
                                      in_delivery=True,
                                      drivers_id=8)
                return redirect('url_sample_list')

class SampleDeliveryView(View):
    def get(self, request):
        sapmles = Sample.objects.order_by("delivery_place_id")
        locations = Location.objects.all()

        paginator = Paginator(sapmles, 40)
        page = request.GET.get("page")
        sample_pag = paginator.get_page(page)
        return render(request, "couriers_panel/sample_delivery.html", {"sample_pag":sample_pag, "locations":locations})
    def post(self, request):
        samples = Sample.objects.all()
        date = datetime.datetime.now()
        date.strftime("%H:%M:%S")
        for sample in samples:
           sample_delivery = request.POST.get(str(sample.id))
           if sample_delivery is not None:
               sample_change = Sample.objects.get(id=sample.id)
               sample_change.in_delivery = False
               sample_change.delivery_date = date
               sample_change.save()
        return redirect('url_sample_list')

class SampleListView(View):
    def get(self, request):
        sapmles = Sample.objects.order_by("delivery_place_id")
        locations = Location.objects.all()

        paginator = Paginator(sapmles, 40)
        page = request.GET.get("page")
        sample_pag = paginator.get_page(page)
        context = {
            "sample_pag": sample_pag,
            "locations": locations,
            "hours": HOURS
        }
        return render(request, "couriers_panel/sample_list.html", context)

class ManagementView(View):
    def get(self, request):
        return render(request, "management_panel/management.html")

class CarsManagementView(View):
    def get(self, request):
        cars = Car.objects.order_by("brand")
        paginator = Paginator(cars, 20)
        page = request.GET.get("page")
        cars_pag = paginator.get_page(page)
        return render(request, "management_panel/cars_management.html", {"cars_pag":cars_pag})

class CarDetailView(View):
    def get(self, request, id):
        car = Car.objects.get(id=id)
        confirm = "Tak"
        if car.fridge == False:
            confirm = "Nie"
        context = {
            "car":car,
            "confirm":confirm
        }
        return render(request, "management_panel/car_details.html", context)

class CarAddView(View):
    def get(self, request):
        return render(request, "management_panel/car_add.html")
    def post(self, request):
        try:
            brand = request.POST.get("brand")
            model = request.POST.get("model")
            tech_review = request.POST.get("tech_review")
            fridge = request.POST.get("fridge")
            couriers_id = int(request.POST.get("couriers_id"))
        except (ValueError):
            return render(request, "management_panel/car_add.html", {'error_message': "Wypełnij poprawnie wszystkie pola."})
        else:
            if brand == "":
                return render(request, "management_panel/car_add.html", {'error_message': "Podaj markę samochodu."})
            elif model == "":
                return render(request, "management_panel/car_add.html", {'error_message': "Podaj model samochodu."})
            elif tech_review == None:
                return render(request, "management_panel/car_add.html", {'error_message': "Podaj datę przeglądu."})
            elif fridge == 'null':
                return render(request, "management_panel/car_add.html", {'error_message': "Podaj czy samochód ma lodówkę?"})
            elif couriers_id == "":
                return render(request, "management_panel/car_add.html", {'error_message': "Podaj opiekuna"})
            else:
                Car.objects.create(brand=brand,
                                   model=model,
                                   tech_review=tech_review,
                                   fridge=fridge,
                                   couriers_id=couriers_id)
            return redirect("/management/cars/")

class CarModyfyView(View):
    def get(self, request, id):
        try:
            car = Car.objects.get(id=id)
            return render(request, "management_panel/car_modyfy.html", {"car":car})
        except:
            return render(request, "management_panel/car_modyfy.html", {"error_message": "Nie można wyświetlić szczegółów."})
    def post(self, request, id):
        try:
            brand_change = request.POST.get("brand")
            model_change = request.POST.get("model")
            tech_review_change = request.POST.get("tech_review")
            fridge_change = request.POST.get("fridge")
            couriers_id_change = int(request.POST.get("couriers_id"))
            car_change = Car.objects.get(id=id)
            car_change.brand = brand_change
            car_change.model = model_change
            car_change.tech_review = tech_review_change
            car_change.fridge = fridge_change
            car_change.couriers_id = couriers_id_change
            car_change.save()
            return redirect('url_cars_management')
        except:
            return render(request, "management_panel/car_modyfy.html", {"error_message": "Nie można zapisać danych."})

class DriversManagementView(View):
    def get(self, request):
        drivers = Courier.objects.order_by("id")
        paginator = Paginator(drivers, 20)
        page = request.GET.get("page")
        drivers_pag = paginator.get_page(page)
        return render(request, "management_panel/drivers_management.html", {"drivers_pag":drivers_pag})

class DriverDetailView(View):
    def get(self, request, id):
        driver = Courier.objects.get(id=id)
        return render(request, "management_panel/driver_details.html", {"driver":driver})

class DriverAddView(View):
    def get(self, request):
        return render(request, "management_panel/driver_add.html")
    def post(self, request):
        try:
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            courier_id = request.POST.get("courier_id")
        except (ValueError):
            return render(request, "management_panel/driver_add.html", {'error_message': "Wypełnij poprawnie wszystkie pola."})
        else:
            if name == "":
                return render(request, "management_panel/driver_add.html", {'error_message': "Podaj imię kierowcy."})
            elif surname == "":
                return render(request, "management_panel/driver_add.html", {'error_message': "Podaj nazwisko kierowcy."})
            elif courier_id == "":
                return render(request, "management_panel/driver_add.html", {'error_message': "Podaj identyfikator kierowcy."})
            else:
                Courier.objects.create(name=name,
                                       surname=surname,
                                       courier_id=courier_id)
            return redirect("/management/drivers/")

class DriverModyfyView(View):
    def get(self, request, id):
        try:
            driver = Courier.objects.get(id=id)
            return render(request, "management_panel/driver_modyfy.html", {"driver":driver})
        except:
            return render(request, "management_panel/driver_modyfy.html", {"error_message": "Nie można wyświetlić szczegółów."})
    def post(self, request, id):
        try:
            name_change = request.POST.get("name")
            surname_change = request.POST.get("surname")
            courier_id_change = request.POST.get("courier_id")
            driver_change = Courier.objects.get(id=id)
            driver_change.name = name_change
            driver_change.surname = surname_change
            driver_change.courier_id = courier_id_change
            driver_change.save()
            return redirect('url_drivers_management')
        except:
            return render(request, "management_panel/driver_modyfy.html", {"error_message": "Nie można zapisać danych."})

class LocationsManagementView(View):
    def get(self, request):
        locations = Location.objects.order_by("id")
        paginator = Paginator(locations, 20)
        page = request.GET.get("page")
        locations_pag = paginator.get_page(page)
        context = {
            "locations_pag":locations_pag,
            "places":PLACE
        }
        return render(request, "management_panel/locations_management.html", context)

class LocationDetailView(View):
    def get(self, request, id):
        location = Location.objects.get(id=id)
        context = {
            "location": location,
            "place":PLACE,
            "hours":HOURS,
            "day":DAY
        }
        return render(request, "management_panel/location_details.html", context)

class LocationAddView(View):
    def get(self, request):
        context = {
            "places": PLACE,
            "hours": HOURS,
            "days": DAY
        }
        return render(request, "management_panel/location_add.html", context)
    def post(self, request):
        try:
            address = request.POST.get("address")
            place = request.POST.get("place")
            pickup_time = request.POST.get("pickup_time")
            pickup_day = request.POST.get("pickup_day")
        except (ValueError):
            return render(request, "management_panel/location_add.html", {'error_message': "Wypełnij poprawnie wszystkie pola."})
        else:
            if address == "":
                return render(request, "management_panel/location_add.html", {'error_message': "Podaj adres lokacji."})
            else:
                Location.objects.create(address=address,
                                        place=place,
                                        pickup_time=pickup_time,
                                        pickup_day=pickup_day)
            return redirect("/management/locations/")

class LocationModyfyView(View):
    def get(self, request, id):
        try:
            location = Location.objects.get(id=id)
            context = {
                "places": PLACE,
                "hours": HOURS,
                "days": DAY,
                "location":location
            }

            return render(request, "management_panel/location_modyfy.html", context)
        except:
            return render(request, "management_panel/location_modyfy.html", {"error_message": "Nie można wyświetlić szczegółów."})
    def post(self, request, id):
        try:
            address_change = request.POST.get("address")
            place_change = request.POST.get("place")
            pickup_time_change = request.POST.get("pickup_time")
            pickup_day_change = request.POST.get("pickup_day")
            location_change = Location.objects.get(id=id)
            location_change.address = address_change
            location_change.place = place_change
            location_change.pickup_time = pickup_time_change
            location_change.pickup_day = pickup_day_change
            location_change.save()
            return redirect('url_locations_management')
        except:
            return render(request, "management_panel/location_modyfy.html", {"error_message": "Nie można zapisać danych."})