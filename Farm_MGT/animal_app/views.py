from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import (Animal, HealthRecord, BreedingRecord, DietPlan, FoodInventory, FeedSchedule, Vaccination, Disease,
                     VetRecord, Stock, Equipment, Task, Customer, Sale)
from .forms import (AnimalForm, HealthRecordForm, BreedingRecordForm, DietPlanForm, FoodInventoryForm, FeedScheduleForm,
                    VaccinationForm, DiseaseForm, VetRecordForm, StockForm, EquipmentForm, TaskForm, CustomerForm, SaleForm)

# Homepage View
def home(request):
    return render(request, 'animal_app/homepage.html')

# Animal Views
def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animal_app/animal_list.html', {'animals': animals})

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'animal_app/animal_detail.html', {'animal': animal})

def animal_create(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm()
    return render(request, 'animal_app/animal_form.html', {'form': form})

def animal_update(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == "POST":
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal_detail', pk=pk)
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'animal_app/animal_form.html', {'form': form})

def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == "POST":
        animal.delete()
        return redirect('animal_list')
    return render(request, 'animal_app/animal_confirm_delete.html', {'object': animal})

# HealthRecord Views
def health_record_list(request):
    health_records = HealthRecord.objects.all()
    return render(request, 'animal_app/health_record_list.html', {'health_records': health_records})

def health_record_detail(request, pk):
    health_record = get_object_or_404(HealthRecord, pk=pk)
    return render(request, 'animal_app/health_record_detail.html', {'health_record': health_record})

def health_record_create(request):
    if request.method == "POST":
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('health_record_list')
    else:
        form = HealthRecordForm()
    return render(request, 'animal_app/health_record_form.html', {'form': form})

def health_record_update(request, pk):
    health_record = get_object_or_404(HealthRecord, pk=pk)
    if request.method == "POST":
        form = HealthRecordForm(request.POST, instance=health_record)
        if form.is_valid():
            form.save()
            return redirect('animal_app/health_record_detail', pk=pk)
    else:
        form = HealthRecordForm(instance=health_record)
    return render(request, 'animal_app/health_record_form.html', {'form': form})

def health_record_delete(request, pk):
    health_record = get_object_or_404(HealthRecord, pk=pk)
    if request.method == "POST":
        health_record.delete()
        return redirect('health_record_list')
    return render(request, 'animal_app/health_record_confirm_delete.html', {'object': health_record})

# BreedingRecord Views
def breeding_record_list(request):
    breeding_records = BreedingRecord.objects.all()
    return render(request, 'animal_app/breeding_record_list.html', {'breeding_records': breeding_records})

def breeding_record_detail(request, pk):
    breeding_record = get_object_or_404(BreedingRecord, pk=pk)
    return render(request, 'animal_app/breeding_record_detail.html', {'breeding_record': breeding_record})

def breeding_record_create(request):
    if request.method == "POST":
        form = BreedingRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('breeding_record_list')
    else:
        form = BreedingRecordForm()
    return render(request, 'animal_app/breeding_record_form.html', {'form': form})

def breeding_record_update(request, pk):
    breeding_record = get_object_or_404(BreedingRecord, pk=pk)
    if request.method == "POST":
        form = BreedingRecordForm(request.POST, instance=breeding_record)
        if form.is_valid():
            form.save()
            return redirect('animal_app/breeding_record_detail', pk=pk)
    else:
        form = BreedingRecordForm(instance=breeding_record)
    return render(request, 'breeding_record_form.html', {'form': form})

def breeding_record_delete(request, pk):
    breeding_record = get_object_or_404(BreedingRecord, pk=pk)
    if request.method == "POST":
        breeding_record.delete()
        return redirect('animal_app/breeding_record_list')
    return render(request, 'animal_app/breeding_record_confirm_delete.html', {'object': breeding_record})

# DietPlan Views
def diet_plan_list(request):
    diet_plans = DietPlan.objects.all()
    return render(request, 'animal_app/diet_plan_list.html', {'diet_plans': diet_plans})

def diet_plan_detail(request, pk):
    diet_plan = get_object_or_404(DietPlan, pk=pk)
    return render(request, 'animal_app/diet_plan_detail.html', {'diet_plan': diet_plan})

def diet_plan_create(request):
    if request.method == "POST":
        form = DietPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diet_plan_list')
    else:
        form = DietPlanForm()
    return render(request, 'animal_app/diet_plan_form.html', {'form': form})

def diet_plan_update(request, pk):
    diet_plan = get_object_or_404(DietPlan, pk=pk)
    if request.method == "POST":
        form = DietPlanForm(request.POST, instance=diet_plan)
        if form.is_valid():
            form.save()
            return redirect('diet_plan_detail', pk=pk)
    else:
        form = DietPlanForm(instance=diet_plan)
    return render(request, 'animal_app/diet_plan_form.html', {'form': form})

def diet_plan_delete(request, pk):
    diet_plan = get_object_or_404(DietPlan, pk=pk)
    if request.method == "POST":
        diet_plan.delete()
        return redirect('diet_plan_list')
    return render(request, 'animal_app/diet_plan_confirm_delete.html', {'object': diet_plan})

# FoodInventory Views
def food_inventory_list(request):
    food_inventory = FoodInventory.objects.all()
    return render(request, 'food_inventory_list.html', {'food_inventory': food_inventory})

def food_inventory_detail(request, pk):
    food_item = get_object_or_404(FoodInventory, pk=pk)
    return render(request, 'animal_app/food_inventory_detail.html', {'food_item': food_item})

def food_inventory_create(request):
    if request.method == "POST":
        form = FoodInventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_inventory_list')
    else:
        form = FoodInventoryForm()
    return render(request, 'animal_app/food_inventory_form.html', {'form': form})

def food_inventory_update(request, pk):
    food_item = get_object_or_404(FoodInventory, pk=pk)
    if request.method == "POST":
        form = FoodInventoryForm(request.POST, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('animal_app/food_inventory_detail', pk=pk)
    else:
        form = FoodInventoryForm(instance=food_item)
    return render(request, 'animal_app/food_inventory_form.html', {'form': form})

def food_inventory_delete(request, pk):
    food_item = get_object_or_404(FoodInventory, pk=pk)
    if request.method == "POST":
        food_item.delete()
        return redirect('food_inventory_list')
    return render(request, 'animal_app/food_inventory_confirm_delete.html', {'object': food_item})

# FeedSchedule Views
def feed_schedule_list(request):
    feed_schedules = FeedSchedule.objects.all()
    return render(request, 'animal_app/feed_schedule_list.html', {'feed_schedules': feed_schedules})

def feed_schedule_detail(request, pk):
    feed_schedule = get_object_or_404(FeedSchedule, pk=pk)
    return render(request, 'animal_app/feed_schedule_detail.html', {'feed_schedule': feed_schedule})

def feed_schedule_create(request):
    if request.method == "POST":
        form = FeedScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feed_schedule_list')
    else:
        form = FeedScheduleForm()
    return render(request, 'animal_app/feed_schedule_form.html', {'form': form})

def feed_schedule_update(request, pk):
    feed_schedule = get_object_or_404(FeedSchedule, pk=pk)
    if request.method == "POST":
        form = FeedScheduleForm(request.POST, instance=feed_schedule)
        if form.is_valid():
            form.save()
            return redirect('feed_schedule_detail', pk=pk)
    else:
        form = FeedScheduleForm(instance=feed_schedule)
    return render(request, 'animal_app/feed_schedule_form.html', {'form': form})

def feed_schedule_delete(request, pk):
    feed_schedule = get_object_or_404(FeedSchedule, pk=pk)
    if request.method == "POST":
        feed_schedule.delete()
        return redirect('feed_schedule_list')
    return render(request, 'animal_app/feed_schedule_confirm_delete.html', {'object': feed_schedule})

# Vaccination Views
def vaccination_list(request):
    vaccinations = Vaccination.objects.all()
    return render(request, 'animal_app/vaccination_list.html', {'vaccinations': vaccinations})

def vaccination_detail(request, pk):
    vaccination = get_object_or_404(Vaccination, pk=pk)
    return render(request, 'animal_app/vaccination_detail.html', {'vaccination': vaccination})

def vaccination_create(request):
    if request.method == "POST":
        form = VaccinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vaccination_list')
    else:
        form = VaccinationForm()
    return render(request, 'animal_app/vaccination_form.html', {'form': form})

def vaccination_update(request, pk):
    vaccination = get_object_or_404(Vaccination, pk=pk)
    if request.method == "POST":
        form = VaccinationForm(request.POST, instance=vaccination)
        if form.is_valid():
            form.save()
            return redirect('animal_app/vaccination_detail', pk=pk)
    else:
        form = VaccinationForm(instance=vaccination)
    return render(request, 'animal_app/vaccination_form.html', {'form': form})

def vaccination_delete(request, pk):
    vaccination = get_object_or_404(Vaccination, pk=pk)
    if request.method == "POST":
        vaccination.delete()
        return redirect('vaccination_list')
    return render(request, 'animal_app/vaccination_confirm_delete.html', {'object': vaccination})

# Disease Views
def disease_list(request):
    diseases = Disease.objects.all()
    return render(request, 'animal_app/disease_list.html', {'diseases': diseases})

def disease_detail(request, pk):
    disease = get_object_or_404(Disease, pk=pk)
    return render(request, 'animal_app/disease_detail.html', {'disease': disease})

def disease_create(request):
    if request.method == "POST":
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease_list')
    else:
        form = DiseaseForm()
    return render(request, 'animal_app/disease_form.html', {'form': form})

def disease_update(request, pk):
    disease = get_object_or_404(Disease, pk=pk)
    if request.method == "POST":
        form = DiseaseForm(request.POST, instance=disease)
        if form.is_valid():
            form.save()
            return redirect('disease_detail', pk=pk)
    else:
        form = DiseaseForm(instance=disease)
    return render(request, 'animal_app/disease_form.html', {'form': form})

def disease_delete(request, pk):
    disease = get_object_or_404(Disease, pk=pk)
    if request.method == "POST":
        disease.delete()
        return redirect('disease_list')
    return render(request, 'animal_app/disease_confirm_delete.html', {'object': disease})

# VetRecord Views
def vet_record_list(request):
    vet_records = VetRecord.objects.all()
    return render(request, 'animal_app/vet_record_list.html', {'vet_records': vet_records})

def vet_record_detail(request, pk):
    vet_record = get_object_or_404(VetRecord, pk=pk)
    return render(request, 'animal_app/vet_record_detail.html', {'vet_record': vet_record})

def vet_record_create(request):
    if request.method == "POST":
        form = VetRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vet_record_list')
    else:
        form = VetRecordForm()
    return render(request, 'vet_record_form.html', {'form': form})

def vet_record_update(request, pk):
    vet_record = get_object_or_404(VetRecord, pk=pk)
    if request.method == "POST":
        form = VetRecordForm(request.POST, instance=vet_record)
        if form.is_valid():
            form.save()
            return redirect('vet_record_detail', pk=pk)
    else:
        form = VetRecordForm(instance=vet_record)
    return render(request, 'animal_app/vet_record_form.html', {'form': form})

def vet_record_delete(request, pk):
    vet_record = get_object_or_404(VetRecord, pk=pk)
    if request.method == "POST":
        vet_record.delete()
        return redirect('vet_record_list')
    return render(request, 'animal_app/vet_record_confirm_delete.html', {'object': vet_record})

# Stock Views
def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'animal_app/stock_list.html', {'stocks': stocks})

def stock_detail(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'animal_app/stock_detail.html', {'stock': stock})

def stock_create(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = StockForm()
    return render(request, 'animal_app/stock_form.html', {'form': form})

def stock_update(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock_detail', pk=pk)
    else:
        form = StockForm(instance=stock)
    return render(request, 'animal_app/stock_form.html', {'form': form})

def stock_delete(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        stock.delete()
        return redirect('stock_list')
    return render(request, 'animal_app/stock_confirm_delete.html', {'object': stock})

# Equipment Views
def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'animal_app/equipment_list.html', {'equipment': equipment})

def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    return render(request, 'animal_app/equipment_detail.html', {'equipment': equipment})

def equipment_create(request):
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'animal_app/equipment_form.html', {'form': form})

def equipment_update(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == "POST":
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_detail', pk=pk)
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'animal_app/equipment_form.html', {'form': form})

def equipment_delete(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == "POST":
        equipment.delete()
        return redirect('equipment_list')
    return render(request, 'animal_app/equipment_confirm_delete.html', {'object': equipment})

# Task Views
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'animal_app/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'animal_app/task_detail.html', {'task': task})

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'animal_app/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'animal_app/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'animal_app/task_confirm_delete.html', {'object': task})

# Customer Views
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'animal_app/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'animal_app/customer_detail.html', {'customer': customer})

def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'animal_app/customer_form.html', {'form': form})

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', pk=pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'animal_app/customer_form.html', {'form': form})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('customer_list')
    return render(request, 'animal_app/customer_confirm_delete.html', {'object': customer})

# Sale Views
def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'animal_app/sale_list.html', {'sales': sales})

def sale_detail(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    return render(request, 'animal_app/sale_detail.html', {'sale': sale})

def sale_create(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = SaleForm()
    return render(request, 'animal_app/sale_form.html', {'form': form})

def sale_update(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == "POST":
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('sale_detail', pk=pk)
    else:
        form = SaleForm(instance=sale)
    return render(request, 'animal_app/sale_form.html', {'form': form})

def sale_delete(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == "POST":
        sale.delete()
        return redirect('sale_list')
    return render(request, 'animal_app/sale_confirm_delete.html', {'object': sale})
