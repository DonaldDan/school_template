from ast import keyword
import code
from pyexpat import model
from tkinter import CASCADE
from turtle import mode, update
from typing_extensions import Self
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
#from django.db.models import National,Extra_County,Sub_County
from django.contrib.auth.models import User

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    selected = models.ManyToManyField(User, related_name='schools', blank=True)
    def __str__(self):
        return self.name

#class County(models.Model):
    #type = models.ForeignKey()
    #name = models.CharField(max_length=200)
    #county = models.CharField(max_length=50, null=True,blank=True)
    #parformance = models.CharField(max_length=20)


class National(models.Model):
    #host=
    topic = models.ForeignKey(School,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    schoolCode = models.CharField(max_length=30)
    county = models.CharField(max_length=50, null=True,blank=True)
    National_code = models.CharField(max_length=50, null=True,blank=True)
    parformance = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class ExtraCounty(models.Model):
    #host=
    topic = models.ForeignKey(School,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    schoolCode = models.CharField(max_length=30)
    county = models.CharField(max_length=50, null=True,blank=True)
    extra_county_code = models.CharField(max_length=50, null=True,blank=True)
    parformance = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class County(models.Model):
    #host=
    topic = models.ForeignKey(School,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    schoolCode = models.CharField(max_length=30)
    county = models.CharField(max_length=50, null=True,blank=True)
    county_code = models.CharField(max_length=50, null=True,blank=True)
    parformance = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SubCounty(models.Model):
    #host=
    topic = models.ForeignKey(School,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    schoolCode = models.CharField(max_length=30)
    county = models.CharField(max_length=50, null=True,blank=True)
    sub_county_code = models.CharField(max_length=50, null=True,blank=True)
    subcounty = models.CharField(max_length=50, null=True,blank=True)
    parformance = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Result(models.Model):
    name = models.ForeignKey(School,on_delete=models.SET_NULL, null=True)
    school_Name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self) -> str:
        return self.name