# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Link(models.Model):
    id = models.OneToOneField('Recipe', models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    email = models.ForeignKey('Users', models.DO_NOTHING, db_column='email', to_field=None)

    class Meta:
        managed = False
        db_table = 'LINK'


class Recipe(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RECIPE'


class Users(models.Model):
    email = models.TextField(primary_key=True)
    password = models.TextField()
    displayname = models.TextField()

    class Meta:
        managed = False
        db_table = 'USERS'
