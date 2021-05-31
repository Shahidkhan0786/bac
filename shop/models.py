from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField
product_choices = [
        ('mobo', 'mobo'),
        ('ram', 'ram'),
        ('processor', 'processor'),
        ('graphicCard', 'graphic-card'),
        ('storage', 'storage'),
        ('powersupply', 'powersupply'),
        ('case', 'case'),
    ]

class Category(models.Model):
    name = models.CharField(max_length=50 , choices=product_choices)


    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    def __str__(self):
        return self.name




class Customer(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    city= models.CharField(max_length=250)
    zipcode=models.CharField(max_length=250)
    Address1 = models.CharField(max_length=50)
    mobile= models.CharField(max_length=50)


    # @staticmethod
    # def get_customer_by_email(email):
    #     try:
    #         return Customer.objects.get(email=email)
    #     except:
    #         return False

    # def isExists(self):
    #     if Customer.objects.filter(email=self.email):
    #         return True
    #
    #     return False
    #
    # def register(self):
    #     self.save()

class vendor(models.Model):
    vendor_name=models.CharField(max_length=250)

    def __str__(self):
        return self.vendor_name


class Case(models.Model):
    vendor = models.ForeignKey(vendor , on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="uploads")
    price = models.IntegerField(default=0 ,null=True)
    dprice = models.FloatField(default=0, null=True, blank=True)
    desc = models.CharField(max_length=200, default="" ,null=True)
    Form_Factor = models.CharField(max_length=250 ,null=True,default="Micro ATX", choices=(("Mini ATX","Mini ATX"),("Micro ATX","Micro ATX"), ("ATX","ATX") , ("E-ATX","E-ATX")))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', null=True, blank=True)



class socket(models.Model):
    socket_type = models.CharField(max_length=250)
    def __str__(self):
        return self.socket_type

class chipset(models.Model):
    cpu_chipset=models.CharField(max_length=250)
    def __str__(self):
        return self.cpu_chipset

class CPU(models.Model):
    image = models.ImageField(upload_to="uploads")
    vendor = models.ForeignKey(vendor , on_delete=models.CASCADE)
    cpu_name=models.CharField(max_length=250)
    cpu_price = models.IntegerField(default="")
    dprice = models.FloatField(default=0, null=True, blank=True)
    desc = models.TextField( default="", null=True)

    generation = models.CharField(max_length=250)
    socket= models.ForeignKey(socket ,on_delete=models.CASCADE)
    chipset =models.ManyToManyField(chipset)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', null=True, blank=True)

    def __str__(self):
        return self.cpu_name


class Storage(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="uploads")
    vendor=models.ForeignKey(vendor , on_delete=CASCADE)
    price = models.IntegerField(default="")
    dprice = models.FloatField(default=0, null=True, blank=True)
    desc = models.TextField( default="", null=True)
    storage_type =models.CharField(max_length=250 ,default="SATA", choices=(("SATA","SATA"), ("IDE","IDE"), ("M.2","M.2")))
    memory = models.CharField(max_length=250 ,default="500GB", choices=(("500GB","500GB"), ("1TB","1TB"), ("2TB","2TB"), ("2TB","2TB"), ("5TB","5TB")))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', null=True, blank=True)

    def __str__(self):
        return self.name



class Motherboard(models.Model):
    mobo_name= models.CharField(max_length=250)
    image = models.ImageField(upload_to="uploads")
    chipset = models.ForeignKey(chipset , on_delete=models.CASCADE)
    socket = models.ForeignKey(socket ,on_delete=models.CASCADE)
    vendor = models.ForeignKey(vendor , on_delete=models.CASCADE)
    price = models.IntegerField(default="")
    dprice = models.FloatField(default=0, null=True, blank=True)
    desc = models.TextField(default="", null=True)
    DIMM_sockets  = models.CharField(max_length=250 ,default="single", choices=(("dual","dual"), ("single","single"),("4","4"),("8","8")))
    Supported_ram= models.CharField(max_length=250 ,default="ddr3", choices=(("ddr2","ddr2"),("ddr3","ddr3"), ("ddr4","ddr4")))
    max_mhz =models.CharField(max_length=250)
    Form_Factor = models.CharField(max_length=250 ,default="Micro ATX", choices=(("Mini ATX","Mini ATX"),("Micro ATX","Micro ATX"), ("ATX","ATX") , ("E-ATX","E-ATX")))
    Onboard_Graphics= models.CharField(max_length=250,blank=True,null=True)
    Expensions_socket_version= models.CharField(max_length=250 ,default="version 1", choices=(("version 1","version 1"), ("version 2","version 2"), ("version 3","version 3"), ("version 4","version 4")))
    Audio =models.CharField(max_length=250,blank=True,null=True)
    LAN =models.CharField(max_length=250 ,blank=True,null=True)
    Storage_Interface =models.ManyToManyField(Storage , default="")
    USB =models.TextField(max_length=250 ,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='',null=True, blank=True)

    def __str__(self):
        return self.mobo_name


class ram(models.Model):
    image = models.ImageField(upload_to="uploads")
    name = models.CharField(max_length=250)
    price = models.IntegerField(default=0, null=True)
    dprice = models.FloatField(default=0, null=True, blank=True)
    desc = models.TextField(default="", null=True)
    vendor = models.ForeignKey(vendor ,on_delete=models.CASCADE)
    type = models.CharField(max_length=250 ,default="ddr3", choices=(("ddr3","ddr3"), ("ddr4","ddr4")))
    mhz =  models.CharField(max_length=250 ,default="1600", choices=(("1600","1600"), ("2400","2400"),("2600","2600"),("2800","2800"),("3200","3200")))
    memory = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', null=True, blank=True)




class Display_ports(models.Model):
    port = models.CharField(max_length=250 ,default="HDMI", choices=(("HDMI","HDMI"), ("VGA","VGA"), ("DVI","DVI"), ("DISPLAY","DISPLAY")))

    def __str__(self):
        return self.port




class Graphic_Card(models.Model):
    name=models.CharField(max_length=250)
    image = models.ImageField(upload_to="uploads")
    vendor = models.ForeignKey(vendor , on_delete=models.CASCADE)
    Memory= models.CharField(max_length=250 ,default="2GB", choices=(("2GB","2GB"), ("4GB","4GB"), ("8GB","8GB")))
    price = models.IntegerField(default="")
    dprice = models.FloatField(default=0, null=True, blank=True)
    desc = models.TextField(default="", null=True)
    version= models.CharField(max_length=250 ,default="version 1", choices=(("version 1","version 1"), ("version 2","version 2"), ("version 3","version 3")))
    recommended_watt = models.CharField(max_length=250 , default='')
    dis_ports= models.ManyToManyField(Display_ports)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', null=True, blank=True)

    def __str__(self):
        return self.name


class Smps(models.Model):
    vendor= models.ForeignKey(vendor , on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads")
    name= models.CharField(max_length=250)
    watt = models.CharField(max_length=250 ,default="250", choices=(("250","250"), ("400","400"), ("450","450"), ("500","500"), ("600","600"), ("750","750"), ("800","800"), ("1000","1000")))
    price = models.IntegerField(default="")
    dprice = models.FloatField(default=0, null=True, blank=True)
    desc = models.TextField(default="", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', null=True, blank=True)

    def __str__(self):
        return self.name







class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    dprice = models.FloatField(default=0, null=True ,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='',choices=product_choices, null=True, blank=True)
    desc = models.TextField(default="")
    prating = models.IntegerField(default=0 , null=True ,blank=True)
    image = models.ImageField(upload_to='products')
    case_id=models.ForeignKey(Case , on_delete=models.CASCADE  , null=True)
    cpu_id=models.ForeignKey(CPU , on_delete=models.CASCADE ,null=True)
    ram_id=models.ForeignKey(ram , on_delete=models.CASCADE , null=True)
    mobo_id=models.ForeignKey(Motherboard , on_delete=models.CASCADE , null=True)
    graphic_id = models.ForeignKey(Graphic_Card, on_delete=models.CASCADE, null=True)
    psu_id = models.ForeignKey(Smps, on_delete=models.CASCADE, null=True)
    storage_id = models.ForeignKey(Storage, on_delete=models.CASCADE, null=True)
    @staticmethod
    def get_all_products_byid(category_id):
        if category_id:
            return Product.objects.filter(category_id)
        else:
            return Product.objects.all()

    @staticmethod
    def get_all_products():
        return Product.objects.all()



class Review(models.Model):
    product_name = models.ForeignKey(to=Product, on_delete=CASCADE)
    prev = models.CharField(max_length=50)
    cr_date = models.DateTimeField(auto_now_add=True)
    review_by = models.ForeignKey(to=User, on_delete=CASCADE)




class MyProfile(models.Model):
    name = models.CharField(max_length = 100)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    city=models.CharField(max_length=250,null=True,default="")
    zipcode=models.CharField(max_length=250 , null=True)
    address = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default="single", choices=(("single","single"), ("married","married"), ("widow","widow"), ("seprated","seprated"), ("commited","commited")))
    gender = models.CharField(max_length=20, default="female", choices=(("male","male"), ("female","female")))
    phone_no = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    pic=models.ImageField(upload_to = "uploads", null=True)

    def __str__(self):
        return "%s" % self.user









# save user build
class Build_PC(models.Model):
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    cpu = models.CharField(max_length=250)
    Mobo=models.CharField(max_length=250)
    ram =models.CharField(max_length=250)
    graphiccard=models.CharField(max_length=250)
    storage = models.CharField(max_length=250)
    power_supply = models.CharField(max_length=250)
    image = models.ImageField(upload_to="uploads" ,default="" ,null=True ,blank='True')
    Chases=models.CharField(max_length=250)




class Wish_List(models.Model):
    user= models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)


GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "female"),
    ("other", "other"),

)


class Vendorx(models.Model):
    # vendor_id =models.AutoField(primary_key=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    mobile = models.CharField(max_length=50, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(null=True, choices=GENDER_CHOICES, max_length=50)
    ShopNmae = models.CharField(max_length=100, null=True)
    cnic= models.ImageField(upload_to="uploads" ,default="" ,null=True ,blank='True')
    age=models.PositiveIntegerField(null=True)


class cart(models.Model):
    person=models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField( default=1)
    @property
    def amount(self):
        return self.quantity * self.product.price


status_choices = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('packed', 'Paceked'),
        ('on the way', 'on the way'),
        ('delivered', 'delivered'),
        ('cancel', 'cancel'),

    ]




class orderplaced(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    product=models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=250 ,choices=status_choices ,null=True)

    @property
    def amount(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.user.username


class builds_guides(models.Model):
    title=models.CharField(max_length=200 )
    introduction = HTMLField()
    note_on_price = HTMLField()
    cpu = HTMLField()
    mobo = HTMLField()
    memory = HTMLField()
    storage= HTMLField()
    gpu=HTMLField()
    case=HTMLField()
    psu=HTMLField()
    image = models.ImageField(upload_to="uploads" ,default="" ,null=True ,blank='True')

    owner=models.ForeignKey(User , on_delete=models.CASCADE)




