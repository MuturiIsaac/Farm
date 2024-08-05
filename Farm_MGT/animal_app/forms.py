from django import forms
from .models import Animal, HealthRecord, BreedingRecord, DietPlan, FoodInventory, FeedSchedule, Vaccination, Disease, VetRecord, Stock, Equipment, Task, Customer, Sale

# Animal Forms
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

# HealthRecord Forms
class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = '__all__'  # Adjust fields as necessary

# BreedingRecord Forms
class BreedingRecordForm(forms.ModelForm):
    class Meta:
        model = BreedingRecord
        fields = '__all__'  # Adjust fields as necessary

# DietPlan Forms
class DietPlanForm(forms.ModelForm):
    class Meta:
        model = DietPlan
        fields = '__all__'  # Adjust fields as necessary

# FoodInventory Forms
class FoodInventoryForm(forms.ModelForm):
    class Meta:
        model = FoodInventory
        fields = '__all__'  # Adjust fields as necessary

# FeedSchedule Forms
class FeedScheduleForm(forms.ModelForm):
    class Meta:
        model = FeedSchedule
        fields = '__all__'  # Adjust fields as necessary

# Vaccination Forms
class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = '__all__'  # Adjust fields as necessary

# Disease Forms
class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = '__all__'  # Adjust fields as necessary

# VetRecord Forms
class VetRecordForm(forms.ModelForm):
    class Meta:
        model = VetRecord
        fields = '__all__'  # Adjust fields as necessary

# Stock Forms
class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'  # Adjust fields as necessary

# Equipment Forms
class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'  # Adjust fields as necessary

# Task Forms
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'  # Adjust fields as necessary

# Customer Forms
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'  # Adjust fields as necessary

# Sale Forms
class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'  # Adjust fields as necessary
