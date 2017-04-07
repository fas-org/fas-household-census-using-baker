# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from .household_models import Household


class OwnershipType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Ownership Type'

    def __str__(self):
        return self.type


class WellType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Well Type'

    def __str__(self):
        return self.type


class PowerSource(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Power Source'

    def __str__(self):
        return self.source


class ExchangeNature(models.Model):
    id = models.AutoField(primary_key=True)
    exchange = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Exchange Nature'

    def __str__(self):
        return self.exchange


class OwnershipWellsTubewells(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    ownership_type = models.ForeignKey('OwnershipType', models.DO_NOTHING, db_column='Type of Ownership', blank=True, null=True)
    year_when_installed = models.IntegerField(db_column='Year when installed', blank=True, null=True)
    present_depth = models.IntegerField(db_column='Present Depth', blank=True, null=True)
    original_depth = models.IntegerField(db_column='Original Depth', blank=True, null=True)
    type = models.ForeignKey(WellType, models.DO_NOTHING, db_column='Type', blank=True, null=True)
    power_source = models.ForeignKey(PowerSource, models.DO_NOTHING, db_column='Source of Power', blank=True, null=True)
    installation_cost = models.IntegerField(db_column='Cost of installation', blank=True, null=True)
    finance_source = models.IntegerField(db_column='Source of finance', blank=True, null=True)
    expenses_last_year = models.IntegerField(db_column='Maintenance expenses last year', blank=True, null=True)
    irrigation_crop = models.CharField(max_length=50, db_column='Irrigation Crop', blank=True, null=True)
    irrigation_sale_area = models.IntegerField(db_column='Irrigation Sale Area', blank=True, null=True)
    irrigation_revenue = models.IntegerField(db_column='Irrigation Revenue', blank=True, null=True)
    exchange_nature = models.ForeignKey(ExchangeNature, models.DO_NOTHING, db_column='Nature of Exchange', blank=True, null=True)
    irrigation_land_extent = models.IntegerField(db_column='Irrigation Land Extent', blank=True, null=True)
    comments = models.CharField(max_length=250, db_column='Comments', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Ownership Wells'