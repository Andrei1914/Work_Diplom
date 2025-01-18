from django.db import models
from django.db import models



class Help(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)
    date_publish = models.DateField(blank=True, null=True, auto_now_add=True)
    answer_message = models.CharField(max_length=200, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'help'


class Service(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)
    service = models.CharField(max_length=200, blank=True, null=True)
    date_service = models.DateField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service'


class Users(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    is_verified = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'users'



class Review(models.Model):
    user = models.TextField()
    content = models.TextField()
    date_publish = models.DateField(auto_now_add=True)
    
    class Meta:
        managed = False
        db_table = 'Review'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkExample(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='work_examples')
    date_publish = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title