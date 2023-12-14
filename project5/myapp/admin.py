from django.contrib import admin
from.models import Django_sagar,Cart,Order,Address

# Register your models here.
@admin.register(Django_sagar)
class admin1(admin.ModelAdmin):
    display_list =['name','age']

    def __str__(self):
        return self.name
    
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Address)

# @admin.register(Cart)
# class admin1(admin.ModelAdmin):
#     display_list = '__all__'

#     def __str__(self):
#         return self.name