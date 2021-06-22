from rest_framework import serializers
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from .models import Catagory ,post

class postSerializer(serializers.Serializer):
    post_idd = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=255, default="")
    post_author = serializers.ReadOnlyField()
    slug = serializers.CharField(max_length=130)
    post_catagory = serializers.ReadOnlyField()
    timeStamp = serializers.DateTimeField()
    thumbnail = serializers.ImageField()
    status = serializers.BooleanField()

    content = HTMLField()

    class Meta:
        model =post
        fields = "__all__"

