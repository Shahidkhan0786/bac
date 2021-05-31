from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save,pre_delete
from django.contrib.auth.models import User
from .models import MyProfile,Product,Case,ram,CPU,Storage,Motherboard,Graphic_Card,Smps

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwarg):
    if created:
        MyProfile.objects.create(user = instance, name=instance.username)

@receiver(post_save, sender=Case)
def save_product(sender, instance, created, **kwarg):
    if created:
        Product.objects.create(name = instance.name, price=instance.price ,dprice=instance.dprice ,desc=instance.desc,image=instance.image,category=instance.category ,case_id=instance)




@receiver(pre_delete, sender=Case)
def del_product(sender, instance, **kwargs):
    Product.objects.get(case_id=instance).delete()


@receiver(post_save, sender=ram)
def save_ram(sender, instance, created, **kwarg):
    if created:
        Product.objects.create(name = instance.name, price=instance.price ,dprice=instance.dprice ,desc=instance.desc,image=instance.image,category=instance.category ,ram_id=instance)


@receiver(post_save, sender=CPU)
def save_cpu(sender, instance, created, **kwarg):
    if created:
        Product.objects.create(name = instance.cpu_name, price=instance.cpu_price ,dprice=instance.dprice ,desc=instance.desc,image=instance.image,category=instance.category ,cpu_id=instance)


@receiver(post_save, sender=Storage)
def save_storage(sender, instance, created, **kwarg):
    if created:
        Product.objects.create(name = instance.name, price=instance.price ,dprice=instance.dprice ,desc=instance.desc,image=instance.image,category=instance.category ,storage_id=instance)





@receiver(post_save, sender=Motherboard)
def save_mobo(sender, instance, created, **kwarg):
    if created:
        Product.objects.create(name = instance.mobo_name, price=instance.price ,dprice=instance.dprice ,desc=instance.desc,image=instance.image,category=instance.category ,mobo_id=instance)


@receiver(post_save, sender=Graphic_Card)
def save_Gpu(sender, instance, created, **kwarg):
    if created:
        Product.objects.create(name = instance.name, price=instance.price ,dprice=instance.dprice ,desc=instance.desc,image=instance.image,category=instance.category ,graphic_id=instance)




@receiver(post_save, sender=Smps)
def save_psu(sender, instance, created, **kwarg):
    if created:
        Product.objects.create(name = instance.name, price=instance.price ,dprice=instance.dprice ,desc=instance.desc,image=instance.image,category=instance.category ,psu_id=instance)





