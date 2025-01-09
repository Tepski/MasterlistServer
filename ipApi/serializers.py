from rest_framework import serializers
from . models import IPCategory

class IPCategorySrlzr(serializers.ModelSerializer):
    class Meta:
        model = IPCategory
        fields = "__all__"