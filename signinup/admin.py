from django.contrib import admin

# Register your models here.
from .models import Course, Department, Person

admin.site.register(Department)
admin.site.register(Course)
# admin.site.register(Person)


@admin.register(Person)
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birthdate', 'age', 'phone_number', 'email_id', 'address', 'department',
                    'course',
                    'purpose',
                    'material']
