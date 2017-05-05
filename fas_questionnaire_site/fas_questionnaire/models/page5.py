# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from fas_questionnaire.models.common import Units, Crop, Month
from fas_questionnaire.models.page2 import IrrigationSource
from .household_models import Household


class Tenurial(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(db_column='tenurial status', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tenurial'

    def __str__(self):
        return self.status


class HomesteadLand(models.Model):
    id = models.AutoField(primary_key=True)
    land_name = models.CharField(db_column='Land Name', max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Homestead Land'

    def __str__(self):
        return self.land_name


class CroppingPatternAndCropSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    crop_number_first_digit = models.FloatField(db_column='first digit', null=True, blank=True)
    crop_number_second_digit = models.FloatField(db_column='second digit', null=True, blank=True)
    crop = models.ForeignKey(Crop, models.DO_NOTHING, db_column='Crop', blank=True, null=True)
    variety = models.CharField(db_column='Variety', max_length=50, blank=True, null=True)
    tenurial_status = models.ForeignKey(Tenurial, models.DO_NOTHING, db_column='tenurial status', blank=True, null=True)
    crop_homestead_land = models.ForeignKey(HomesteadLand, models.DO_NOTHING, db_column='Crop/ Homestead land',
                                            blank=True, null=True)
    extent = models.FloatField(db_column='Extent', blank=True, null=True)
    month_of_sowing = models.ForeignKey(Month, models.DO_NOTHING, db_column='Month of sowing', blank=True, null=True,
                                        related_name='month_of_sowing')
    month_of_harvesting = models.ForeignKey(Month, models.DO_NOTHING, db_column='Month of harvesting', blank=True,
                                            null=True, related_name='month_of_harvesting')
    source_of_irrigation = models.ForeignKey(IrrigationSource, models.DO_NOTHING, db_column='Source of irrigation',
                                             blank=True, null=True, related_name='source_of_irrigation')

    comments = models.CharField(db_column='Comments', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cropping pattern and crop schedule'


class CroppingPatternAndCropScheduleComments(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    comments_notes = models.TextField(db_column='comments/notes', max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cropping pattern and crop schedule comments'
