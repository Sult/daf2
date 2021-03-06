from django.db import models


class Alliance(models.Model):
    """ group of corporations """

    name = models.CharField(max_length=254, unique=True)
    shortname = models.CharField(max_length=254)
    allianceid = models.BigIntegerField(unique=True)
    executorcorpid = models.BigIntegerField(unique=True)
    membercount = models.IntegerField()
    startdate = models.DateTimeField()

    def __unicode__(self):
        return self.name
