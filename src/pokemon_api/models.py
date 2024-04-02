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
    types = models.ManyToManyField('Type', related_name='pokemons')

    class Meta:
        db_table = 'pokemon'


class Type(models.Model):
    name = models.CharField(max_length=255, null=False)
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'type'

