from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.user_model import User
from .models.admin_model import Admin
from .models.court_model import Court
from .models.reservation_model import Reservation
from .models.review_model import Review
from .models.payment_model import Payment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_id','first_name', 'last_name', 'rol', 'date_register',)
    search_fields = ('email', 'user_id','first_name', 'last_name')
    list_filter = ('rol', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('user_id', 'email', 'password')}),
        ('Información de Contacto', {'fields': ('first_name', 'last_name', 'contact_number', 'address')}),
        ('Rol de Usuario', {'fields': ('rol', 'date_register',)}),
        ('Estado de Usuario', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    readonly_fields = ('date_register',)
    list_per_page = 10

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user',)
    list_per_page = 10 

@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('court_id', 'name', 'location', 'surface_type', 'hourly_rate', 'availability', 'capacity')
    search_fields = ('court_id', 'name', 'location', 'surface_type')
    list_filter = ('surface_type', 'availability')
    ordering = ('court_id',)
    fieldsets = (
        (None, {'fields': ('court_id', 'name', 'location', 'surface_type', 'hourly_rate', 'availability', 'capacity')}),
    )
    readonly_fields = ('court_id',)
    list_per_page = 10

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_id', 'user', 'court', 'reservation_date', 'start_datetime', 'duration_hours', 'status')
    search_fields = ('reservation_id', 'user', 'court')
    list_filter = ('status',)
    ordering = ('reservation_id',)
    fieldsets = (
        (None, {'fields': ('reservation_id', 'user', 'court', 'reservation_date', 'start_datetime', 'duration_hours', 'status')}),
    )
    readonly_fields = ('reservation_id', 'reservation_date')
    list_per_page = 10

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'user', 'court', 'rating', 'comment', 'review_date')
    search_fields = ('review_id', 'user', 'court')
    list_filter = ('rating',)
    ordering = ('review_id',)
    fieldsets = (
        (None, {'fields': ('review_id', 'user', 'court', 'rating', 'comment', 'review_date')}),
    )
    readonly_fields = ('review_id', 'review_date')
    list_per_page = 10

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'reservation', 'amount', 'payment_date', 'payment_method', 'payment_status')
    search_fields = ('payment_id', 'reservation')
    list_filter = ('payment_method', 'payment_status')
    ordering = ('payment_id',)
    fieldsets = (
        (None, {'fields': ('payment_id', 'reservation', 'amount', 'payment_date', 'payment_method', 'payment_status')}),
    )
    readonly_fields = ('payment_id', 'payment_date')
    list_per_page = 10

