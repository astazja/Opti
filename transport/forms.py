from django import forms
from .models import Sample, Car, Courier, Location, Worker

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = '__all__'
        
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
class CourierForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = "__all__"
        
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        
class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = "__all__"