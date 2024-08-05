from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL

    # Animal URLs
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/<int:pk>/', views.animal_detail, name='animal_detail'),
    path('animals/create/', views.animal_create, name='animal_create'),
    path('animals/<int:pk>/edit/', views.animal_update, name='animal_update'),
    path('animals/<int:pk>/delete/', views.animal_delete, name='animal_delete'),

    # HealthRecord URLs
    path('health_records/', views.health_record_list, name='health_record_list'),
    path('health_records/<int:pk>/', views.health_record_detail, name='health_record_detail'),
    path('health_records/create/', views.health_record_create, name='health_record_create'),
    path('health_records/<int:pk>/edit/', views.health_record_update, name='health_record_update'),
    path('health_records/<int:pk>/delete/', views.health_record_delete, name='health_record_delete'),

    # BreedingRecord URLs
    path('breeding_records/', views.breeding_record_list, name='breeding_record_list'),
    path('breeding_records/<int:pk>/', views.breeding_record_detail, name='breeding_record_detail'),
    path('breeding_records/create/', views.breeding_record_create, name='breeding_record_create'),
    path('breeding_records/<int:pk>/edit/', views.breeding_record_update, name='breeding_record_update'),
    path('breeding_records/<int:pk>/delete/', views.breeding_record_delete, name='breeding_record_delete'),

    # DietPlan URLs
    path('diet_plans/', views.diet_plan_list, name='diet_plan_list'),
    path('diet_plans/<int:pk>/', views.diet_plan_detail, name='diet_plan_detail'),
    path('diet_plans/create/', views.diet_plan_create, name='diet_plan_create'),
    path('diet_plans/<int:pk>/edit/', views.diet_plan_update, name='diet_plan_update'),
    path('diet_plans/<int:pk>/delete/', views.diet_plan_delete, name='diet_plan_delete'),

    # FoodInventory URLs
    path('food_inventory/', views.food_inventory_list, name='food_inventory_list'),
    path('food_inventory/<int:pk>/', views.food_inventory_detail, name='food_inventory_detail'),
    path('food_inventory/create/', views.food_inventory_create, name='food_inventory_create'),
    path('food_inventory/<int:pk>/edit/', views.food_inventory_update, name='food_inventory_update'),
    path('food_inventory/<int:pk>/delete/', views.food_inventory_delete, name='food_inventory_delete'),

    # FeedSchedule URLs
    path('feed_schedules/', views.feed_schedule_list, name='feed_schedule_list'),
    path('feed_schedules/<int:pk>/', views.feed_schedule_detail, name='feed_schedule_detail'),
    path('feed_schedules/create/', views.feed_schedule_create, name='feed_schedule_create'),
    path('feed_schedules/<int:pk>/edit/', views.feed_schedule_update, name='feed_schedule_update'),
    path('feed_schedules/<int:pk>/delete/', views.feed_schedule_delete, name='feed_schedule_delete'),

    # Vaccination URLs
    path('vaccinations/', views.vaccination_list, name='vaccination_list'),
    path('vaccinations/<int:pk>/', views.vaccination_detail, name='vaccination_detail'),
    path('vaccinations/create/', views.vaccination_create, name='vaccination_create'),
    path('vaccinations/<int:pk>/edit/', views.vaccination_update, name='vaccination_update'),
    path('vaccinations/<int:pk>/delete/', views.vaccination_delete, name='vaccination_delete'),

    # Disease URLs
    path('diseases/', views.disease_list, name='disease_list'),
    path('diseases/<int:pk>/', views.disease_detail, name='disease_detail'),
    path('diseases/create/', views.disease_create, name='disease_create'),
    path('diseases/<int:pk>/edit/', views.disease_update, name='disease_update'),
    path('diseases/<int:pk>/delete/', views.disease_delete, name='disease_delete'),

    # VetRecord URLs
    path('vet_records/', views.vet_record_list, name='vet_record_list'),
    path('vet_records/<int:pk>/', views.vet_record_detail, name='vet_record_detail'),
    path('vet_records/create/', views.vet_record_create, name='vet_record_create'),
    path('vet_records/<int:pk>/edit/', views.vet_record_update, name='vet_record_update'),
    path('vet_records/<int:pk>/delete/', views.vet_record_delete, name='vet_record_delete'),

    # Stock URLs
    path('stocks/', views.stock_list, name='stock_list'),
    path('stocks/<int:pk>/', views.stock_detail, name='stock_detail'),
    path('stocks/create/', views.stock_create, name='stock_create'),
    path('stocks/<int:pk>/edit/', views.stock_update, name='stock_update'),
    path('stocks/<int:pk>/delete/', views.stock_delete, name='stock_delete'),

    # Equipment URLs
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('equipment/<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('equipment/create/', views.equipment_create, name='equipment_create'),
    path('equipment/<int:pk>/edit/', views.equipment_update, name='equipment_update'),
    path('equipment/<int:pk>/delete/', views.equipment_delete, name='equipment_delete'),

    # Task URLs
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),

    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/edit/', views.customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),

    # Sale URLs
    path('sales/', views.sale_list, name='sale_list'),
    path('sales/<int:pk>/', views.sale_detail, name='sale_detail'),
    path('sales/create/', views.sale_create, name='sale_create'),
    path('sales/<int:pk>/edit/', views.sale_update, name='sale_update'),
    path('sales/<int:pk>/delete/', views.sale_delete, name='sale_delete'),
]
