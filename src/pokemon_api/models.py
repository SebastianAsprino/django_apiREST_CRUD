from django.db import models

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    imagen = models.CharField(max_length=255, null=False)
    hp = models.IntegerField(null=False)
    attack = models.IntegerField(null=False)
    defense = models.IntegerField(null=False)
    speed = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    createdByDB = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = 'pokemon'  # Opcional: especifica el nombre de la tabla si quieres que sea diferente al predeterminado


class Type(models.Model):
    name = models.CharField(max_length=255, null=False)
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'type'  # Especifica el nombre de la tabla si quieres que sea diferente al nombre modelo predeterminado

