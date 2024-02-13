from django.db import models

# Create your models here.
class contacto(models.Model):
    id= models.AutoField(primary_key=True)
    nome=models.CharField(max_length=50)
    apelido=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    telefone=models.IntegerField()


    