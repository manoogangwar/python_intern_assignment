from rest_framework import serializers
from .models import App


#create serializers here
class AppSerializer(serializers.HyperlinkedModelSerializer):
    App_id=serializers.ReadOnlyField()
    class Meta:
        model= App
        fields="__all__"