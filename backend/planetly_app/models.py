from django.db import models

import uuid

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, null=False)
    
    class Meta:
        verbose_name= "User"
        verbose_name_plural= "Users"

class UsageType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    factor = models.FloatField()
    
    class Meta:
        verbose_name= "UsageType"
        verbose_name_plural= "UsageTypes"
        

class Usage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usage_type = models.ForeignKey(UsageType, on_delete=models.CASCADE)
    usage_at = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    
    class Meta:
        verbose_name= "Usage"
        verbose_name_plural= "Usage"
    