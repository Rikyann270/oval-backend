from django.db import models

from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

def upload_location(instance, filename, **kwargs):
    file_path = 'chicks/{filename}'.format(
        filename=filename
    )
    return file_path
    
def upload_location1(instance, filename, **kwargs):
    file_path = 'equipments/{filename}'.format(
        filename=filename
    )
    return file_path

def upload_location2(instance, filename, **kwargs):
    file_path = 'feeds/{filename}'.format(
        filename=filename
    )
    return file_path

def upload_location3(instance, filename, **kwargs):
    file_path = 'vaccines/{filename}'.format(
        filename=filename
    )
    return file_path

class ChickInfor(models.Model):
    name                = models.CharField(max_length=100, unique=True, null=False, blank=False)
    moreInfo            = models.TextField(max_length=5000, null=False, blank=False)
    price               = models.IntegerField(null=False, blank=False)
    dates               = models.CharField(max_length=150, null=False, blank=False)
    Image               = models.ImageField(upload_to=upload_location1, null=False, blank=False)
    slug                = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

class EquipmentsInfor(models.Model):
    name                = models.CharField(max_length=100, unique=True, null=False, blank=False)
    moreInfo            = models.TextField(max_length=5000, null=False, blank=False)
    price               = models.IntegerField(null=False, blank=False)
    Image               = models.ImageField(upload_to=upload_location, null=False, blank=False)
    slug                = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

class FeedsInfor(models.Model):
    name                = models.CharField(max_length=100, unique=True, null=False, blank=False)
    moreInfo            = models.TextField(max_length=5000, null=False, blank=False)
    price               = models.IntegerField(null=False, blank=False)
    Image               = models.ImageField(upload_to=upload_location, null=False, blank=False)
    slug                = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

class VaccineInfor(models.Model):
    name                = models.CharField(max_length=100, unique=True, null=False, blank=False)
    moreInfo            = models.TextField(max_length=5000, null=False, blank=False)
    price               = models.IntegerField(null=False, blank=False)
    Image               = models.ImageField(upload_to=upload_location, null=False, blank=False)
    slug                = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name




@receiver(post_delete, sender=ChickInfor)
def submission_delete(sender, instance, **kwargs):
    instance.Image.delete(False)

@receiver(post_delete, sender=EquipmentsInfor)
def submission_delete(sender, instance, **kwargs):
    instance.Image.delete(False)

@receiver(post_delete, sender=FeedsInfor)
def submission_delete(sender, instance, **kwargs):
    instance.Image.delete(False)

@receiver(post_delete, sender=VaccineInfor)
def submission_delete(sender, instance, **kwargs):
    instance.Image.delete(False)


def pre_save_vaccineInforr_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name  +"_"+ "vaccine")

def pre_save_feedsInforr_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name  +"_"+ "feeds")


def pre_save_chickeninfor_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name  +"_"+ "price")

def pre_save_equipmentsinfor_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name  +"_"+ "tools")




pre_save.connect(pre_save_chickeninfor_receiver, sender=ChickInfor)
pre_save.connect(pre_save_equipmentsinfor_receiver, sender=EquipmentsInfor)
pre_save.connect(pre_save_feedsInforr_receiver, sender=FeedsInfor)
pre_save.connect(pre_save_vaccineInforr_receiver, sender=VaccineInfor)
