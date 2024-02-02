from rest_framework import serializers
from stadium.models import *
from .models import Photo




class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

    def create(self, validated_data):
        return Possibilitie.objects.create(**validated_data)


    

class PossibilitieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Possibilitie
        fields = '__all__'

    def create(self, validated_data):
        return Possibilitie.objects.create(**validated_data)



class SportFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = SportField
        fields = '__all__'

    def create(self, validated_data):
        return SportField.objects.create(**validated_data)




class StudiumSetSerializer(serializers.ModelSerializer):


    class Meta:
        model = StudiumSet
        fields = '__all__'

    def create(self, validated_data):
        return StudiumSet.objects.create(**validated_data)
    

class ClassTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassTime
        fields = '__all__'

    def create(self, validated_data):
        return ClassTime.objects.create(**validated_data)



class WeeklyReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeeklyReservation
        fields = '__all__'

        def create(self, validated_data):
            return WeeklyReservation.objects.create(**validated_data)
