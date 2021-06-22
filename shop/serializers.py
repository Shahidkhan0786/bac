from rest_framework import serializers
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from .models import Build_PC,Product
class builds_guidesSerializer(serializers.Serializer):
    title = serializers.CharField()

    image = serializers.ImageField()
    owner_name = serializers.ReadOnlyField()


class Build_PCSerializer(serializers.Serializer):
    owner_name = serializers.ReadOnlyField()
    cpu =serializers.CharField()
    Mobo =serializers.CharField()
    ram = serializers.CharField()
    graphiccard = serializers.CharField()
    storage = serializers.CharField()
    power_supply = serializers.CharField()
    image =serializers.ImageField()
    Chases =serializers.CharField()
    vote_count = serializers.IntegerField()
    vote_average = serializers.FloatField()

    class Meta:
        model = Build_PC
        fields = "__all__"
#
# class ProductSerializer(serializers.Serializer):
#     namee = serializers.ReadOnlyField()
#
#     class Meta:
#         model= Product
#         fields ="__all__"

#     price = models.IntegerField(default=0)
#     dprice = models.FloatField(default=0, null=True, blank=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', choices=product_choices, null=True,
#                                  blank=True)
#     desc = serializers.TextField(default="")
#     prating = serializers.IntegerField(default=0, null=True, blank=True)
#     image = serializers.ImageField(upload_to='products')
#     case_id = serializers.ForeignKey(Case, on_delete=models.CASCADE, null=True)
#     cpu_id = serializers.ForeignKey(CPU, on_delete=models.CASCADE, null=True)
#     ram_id = serializers.ForeignKey(ram, on_delete=models.CASCADE, null=True)
#     mobo_id = serializers.ForeignKey(Motherboard, on_delete=models.CASCADE, null=True)
#     graphic_id = serializers.ForeignKey(Graphic_Card, on_delete=models.CASCADE, null=True)
#     psu_id = serializers.ForeignKey(Smps, on_delete=models.CASCADE, null=True)
#     storage_id = serializers.ForeignKey(Storage, on_delete=models.CASCADE,



