from django.db import models

# Animal Records Management
class Animal(models.Model):
    identification = models.CharField(max_length=100, unique=True)
    breed = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    
    def __str__(self):
        return f"{self.identification} - {self.breed} - {self.species}"

class HealthRecord(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='health_records')
    date = models.DateField()
    description = models.TextField()
    
    def __str__(self):
        return f"HealthRecord for {self.animal.identification} on {self.date}"

class BreedingRecord(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='breeding_records')
    mate_id = models.CharField(max_length=100)
    breeding_date = models.DateField()
    offspring_count = models.IntegerField()
    
    def __str__(self):
        return f"BreedingRecord for {self.animal.identification} on {self.breeding_date}"

# Feeding and Nutrition
class DietPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class FoodInventory(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class FeedSchedule(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='feed_schedules')
    diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE, related_name='feed_schedules')
    feed_time = models.TimeField()
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    
    def __str__(self):
        return f"FeedSchedule for {self.animal.identification} - {self.feed_time}"

# Animal Health
class Vaccination(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='vaccinations')
    vaccine_name = models.CharField(max_length=100)
    vaccination_date = models.DateField()
    next_due_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"Vaccination for {self.animal.identification} - {self.vaccine_name}"

class Disease(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='diseases')
    disease_name = models.CharField(max_length=100)
    diagnosis_date = models.DateField()
    recovery_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"Disease for {self.animal.identification} - {self.disease_name}"

class VetRecord(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='vet_records')
    vet_name = models.CharField(max_length=100)
    visit_date = models.DateField()
    notes = models.TextField()
    
    def __str__(self):
        return f"VetRecord for {self.animal.identification} by {self.vet_name} on {self.visit_date}"

# Resources
class Stock(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    purchase_date = models.DateField()
    maintenance_schedule = models.TextField()
    
    def __str__(self):
        return self.name

# Task Workflow
class Task(models.Model):
    description = models.TextField()
    assigned_to = models.CharField(max_length=100)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.description

# CRM
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    
    def __str__(self):
        return self.name

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sales')
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='sales')
    sale_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Sale of {self.animal.identification} to {self.customer.name} on {self.sale_date}"
