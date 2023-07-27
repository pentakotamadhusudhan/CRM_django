from django.db import models


rolelist = [
  ("Manager", "Manager"),
  ("Excute", "Excute"),
  ("Bpo", "Bpo"),
  ("Admin", "Admin"),


]


from django.db import models

class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10)
    class Meta:
        db_table="Login"

class Account(models.Model):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=36)
    Created_on = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    Updated_on = models.DateTimeField(verbose_name='date_joined', )
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(choices=rolelist,max_length=100)
    object = models.Manager
    # class Meta:
    #     db_table="Account"


  

