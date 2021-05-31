from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer,cart
from .models import Review
from .models import Smps,Case,MyProfile,vendor,socket,chipset,CPU,Motherboard,Display_ports,ram,Storage,Graphic_Card
from .models import Build_PC,Vendorx,orderplaced,builds_guides

# Register your models here
class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'category','image']

class Product_category(admin.ModelAdmin):
    list_display = ['id' ,'name']

class customer(admin.ModelAdmin):
    list_display = ['id' ]

class MyProfileAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name", "status", "phone_no"]
    list_filter = ["status", "gender"]


class cpuAdmin(admin.ModelAdmin):
    list_display = ["id","cpu_name"]


class socketAdmin(admin.ModelAdmin):
    list_display = ["id","socket_type"]


class moboAdmin(admin.ModelAdmin):
    list_display = ["id","mobo_name","chipset" ,"socket"]


class ramAdmin(admin.ModelAdmin):
    list_display = ["id","name","vendor" ,"type","mhz"]

class smpsAdmin(admin.ModelAdmin):
    list_display = ["id","name","vendor" ,"watt"]

class caseAdmin(admin.ModelAdmin):
    list_display = ["id","name","vendor" ,"Form_Factor"]

class savepcAdmin(admin.ModelAdmin):
    list_display = ["id","owner"]


class vxAdmin(admin.ModelAdmin):
    list_display = ["id","user" ,"ShopNmae"]

class cartAdmin(admin.ModelAdmin):
    list_display = ["id","person" ,"product" ,"quantity"]


admin.site.register(MyProfile, MyProfileAdmin)


admin.site.register(Product, AdminProduct)
admin.site.register(Category , Product_category)
admin.site.register(Customer , customer)
admin.site.register(Review)
admin.site.register(CPU,cpuAdmin)
admin.site.register(Motherboard , moboAdmin)
admin.site.register(socket ,socketAdmin)
admin.site.register(chipset)
admin.site.register(vendor)
admin.site.register(Vendorx ,vxAdmin)
admin.site.register(Display_ports)
admin.site.register(ram ,ramAdmin)
admin.site.register(Storage)
admin.site.register(cart ,cartAdmin)
admin.site.register(Graphic_Card)
admin.site.register(Smps , smpsAdmin)
admin.site.register(Case , caseAdmin)
admin.site.register(Build_PC , savepcAdmin)
admin.site.register(orderplaced )
admin.site.register(builds_guides)