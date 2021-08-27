# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from PIL import Image

class Carbodytype(models.Model):
    carbodyname = models.CharField(db_column='CarBodyName', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.carbodyname

    class Meta:
        managed = False
        db_table = 'carbodytype'


class Carmodel(models.Model):
    modelname = models.CharField(db_column='ModelName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    carvenderid = models.ForeignKey('Carvender', models.DO_NOTHING, db_column='CarVenderID', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.modelname
    class Meta:
        managed = False
        db_table = 'carmodel'


class Carstate(models.Model):
    state = models.CharField(db_column='State', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.state
    class Meta:
        managed = False
        db_table = 'carstate'


class Cart(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    requestid = models.ForeignKey('Sellrequest', models.DO_NOTHING, db_column='RequestId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'


class Carvender(models.Model):
    carvendername = models.CharField(db_column='CarVenderName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.carvendername
    class Meta:
        managed = False
        db_table = 'carvender'


class Drivetype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.type
    class Meta:
        managed = False
        db_table = 'drivetype'


class Fueltype(models.Model):
    fuelname = models.CharField(db_column='FuelName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.fuelname
    class Meta:
        managed = False
        db_table = 'fueltype'


class Gearbox(models.Model):
    gearboxcotype = models.CharField(db_column='GearBoxcoType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.gearboxcotype
    class Meta:
        managed = False
        db_table = 'gearbox'


class Region(models.Model):
    region = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return self.region
    class Meta:
        managed = False
        db_table = 'region'


class Sellrequest(models.Model):

    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    region = models.ForeignKey(Region, models.DO_NOTHING, db_column='Region', blank=True, null=True)  # Field name made lowercase.
    inginvolume = models.FloatField(db_column='InginVolume', blank=True, null=True)  # Field name made lowercase.
    fueltypeid = models.ForeignKey(Fueltype, models.DO_NOTHING, db_column='FuelTypeId', blank=True, null=True)  # Field name made lowercase.
    carbodyid = models.ForeignKey(Carbodytype, models.DO_NOTHING, db_column='CarBodyId', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    drivetypeid = models.ForeignKey(Drivetype, models.DO_NOTHING, db_column='DriveTypeId', blank=True, null=True)  # Field name made lowercase.
    gearboxid = models.ForeignKey(Gearbox, models.DO_NOTHING, db_column='GearBoxId', blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=45, blank=True, null=True)  # Field name made lowercase.
    carmodelid = models.ForeignKey(Carmodel, models.DO_NOTHING, db_column='CarModelId', blank=True, null=True)  # Field name made lowercase.
    carstateid = models.ForeignKey(Carstate, models.DO_NOTHING, db_column='CarStateId', blank=True, null=True)  # Field name made lowercase.
    #CreationDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # image = models.ImageField(default="33.jpg", null=True, blank=True, upload_to='cars_imgs')

    def __str__(self):

        return str(f"{self.carmodelid.modelname},{self.carmodelid.carvenderid.carvendername}")

    def get_absolute_url(self):
      return reverse("sell_detail", kwargs={"pk": self.pk})

    # def save(self,*args,**kwargs):
    #     super().save(*args, **kwargs)
    #     img=Image.open(self.image.path)
    #
    #     if img.height>300 or img.width>300:
    #         img.thumbnail((300,300))
    #         img.save(self.image.path)


    class Meta:
        managed = False
        db_table = 'sellrequest'
        # ordering = ('-CreationDate',)

class User(models.Model):
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    birthday = models.CharField(db_column='Birthday', max_length=45, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    region = models.ForeignKey(Region, models.DO_NOTHING, db_column='Region', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(f"{self.name} {self.surname}")
    class Meta:
        managed = False
        db_table = 'user'
