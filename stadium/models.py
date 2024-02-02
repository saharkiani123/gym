import os
from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import User



class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')



class Possibilitie(models.Model):
    title = models.CharField(max_length=200, default='rakhtkan')
    possibilitie = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Possibilitie')
        verbose_name_plural = _('Possibilities')


class SportField(models.Model):
    title = models.CharField(max_length=200, default='bascketball')
    sportfield = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('SportField')
        verbose_name_plural = _('SportFields')



class StudiumSet(models.Model):

    STATUS_CHOICES = [
        ('تهران', 'تهران'),
        ('اصفهان', 'اصفهان'),
        ('شیراز', 'شیراز'),
        
    ]

    CITY_CHOICES = [
        ('تهران', 'تهران'),
        ('اصفهان', 'اصفهان'),
        ('شیراز', 'شیراز'),
    ]

    AREA_CHOICES = [
        ('تهران', 'تهران'),
        ('اصفهان', 'اصفهان'),
        ('شیراز', 'شیراز'),

    ]


    title = models.CharField(max_length=200, null=True, blank=True)
    rate = models.CharField(max_length=100,null=True, blank=True, default=0)
    number_people_rate = models.IntegerField(default=0)
    sum_rate = models.CharField(max_length=100,null=True, blank=True, default=0)
    possibilitie_id = models.ForeignKey(Possibilitie, on_delete=models.CASCADE, default = '')
    sportfield_id = models.ForeignKey(SportField, on_delete=models.CASCADE, default = '')
    address = models.TextField(max_length=250, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    discount = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)
    city = models.CharField(max_length=20, choices=CITY_CHOICES, null=True, blank=True)
    area = models.CharField(max_length=20, choices=AREA_CHOICES, null=True, blank=True)
    picture = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True, blank=True)

    
    class Meta:
        verbose_name = _('StudiumSet')
        verbose_name_plural = _('StudiumSets')



class ClassTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()



    class Meta:
        verbose_name = _('ClassTime')
        verbose_name_plural = _('ClassTimes')



class WeeklyReservation(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    studiumset_id = models.ForeignKey(StudiumSet, on_delete=models.CASCADE)
    class_time_id = models.ForeignKey(ClassTime, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=[(i, i) for i in range(1, 8)])  # 1: Sunday, 2: Monday, ..., 7: Saturday
    price = models.CharField(max_length=200, null=True, blank=True)
    booking = models.BooleanField(verbose_name=_('در حال رزرو'), default=False)
    booklable = models.BooleanField( verbose_name=_('قابل رزرو'), default=False)
    reserved = models.BooleanField( verbose_name=_('رزرو شده'), default=False)

    class Meta:
        verbose_name = _('WeeklyReservation')
        verbose_name_plural = _('WeeklyReservations')
    