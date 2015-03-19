from django.db import models
#from django.conf import settings

#from config.storage import OverwriteStorage
#from utils.common import icon_size_name
from utils.connection import *


class CorporationApi(models.Model):
    """ charactertype apis """

    api = models.OneToOneField('apies.Api')
    corporationid = models.BigIntegerField()
    corporationname = models.CharField(max_length=254)
    characterid = models.BigIntegerField()

    def __unicode__(self):
        return self.corporationname

#class CorporationIcon(models.Model):
    #""" images related to characters """

    #relation = models.ForeignKey("corporations.Corporation")
    #size = models.IntegerField(choices=settings.IMAGE_SIZES)
    #typeid = models.IntegerField(unique=True)
    #icon = models.ImageField(
        #upload_to="images/corporations/",
        #storage=OverwriteStorage(),
        #blank=True, null=True)

    #class Meta:
        #unique_together = ["size", "relation"]

    #def __unicode__(self):
        #return "Corporation Image %s" % icon_size_name(self.size)


    ##get list of wanted character icon sizes
    #@staticmethod
    #def icon_sizes():
        #return [32, 64, 128, 256]
