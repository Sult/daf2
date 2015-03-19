from datetime import datetime
from collections import namedtuple

from django.db import models
from django.utils.timezone import utc

#from utils import connection
from apps.static.models import Crpnpccorporations, Invnames


class Corporation(models.Model):
    """ group of players in eve working together. Is jsut like a guild in
    other games """

    lastrefresh = models.DateTimeField(null=True)
    corporationid = models.BigIntegerField(unique=True)
    corporationname = models.CharField(max_length=254, unique=True)
    ticker = models.CharField(max_length=254)
    isnpccorp = models.BooleanField(default=False)
    allianceid = models.BigIntegerField(null=True)
    alliancename = models.CharField(max_length=254, blank=True)
    avgsecstatus = models.FloatField(default=0.0)
    ceoid = models.BigIntegerField()
    ceoname = models.CharField(max_length=254)
    stationid = models.BigIntegerField()
    description = models.TextField()
    url = models.URLField(max_length=254)
    taxrate = models.FloatField()
    membercount = models.IntegerField()

    def __unicode__(self):
        return self.corporationName

    #refresh the timer while saving object
    def save(self, *args, **kwargs):
        now = datetime.now().replace(tzinfo=utc)
        self.lastrefresh = now
        super(Corporation, self).save(*args, **kwargs)

    #find a corporation by id (NPC corps included)
    #return the pk, name and npc/player
    @staticmethod
    def find_corporation(corp_id):
        if Crpnpccorporations.objects.filter(corporationid=corp_id).exists():
            corp = Crpnpccorporations.objects.get(corporationid=corp_id)
            name = Invnames.objects.get(itemid=corp_id).itemname
            return name
        elif Corporation.objects.filter(corporationid=corp_id).exists():
            corp = Corporation.objects.get(corporationid=corp_id)
            return corp.corporationname
        else:
            corp = Corporation.create_corporation(corp_id)
            return corp.corporationname

    #create a corp if corporationid does not exist yet
    @staticmethod
    def create_corporation(corp_id):
        corp_data = getattr(connection, "corporationsheet")(corp_id)
        try:
            if corp_data.allianceID == 0:
                allianceid = None
                alliancename = ""
            else:
                allianceid = corp_data.allianceID
                alliancename = corp_data.allianceName

            corp = Corporation.objects.create(
                corporationid=corp_data.corporationID,
                corporationname=corp_data.corporationName,
                ticker=corp_data.ticker,
                ceoid=corp_data.ceoID,
                ceoname=corp_data.ceoName,
                allianceid=allianceid,
                alliancename=alliancename,
                stationid=corp_data.stationID,
                description=unicode(corp_data.description),
                url=corp_data.url,
                taxrate=int(corp_data.taxRate),
                membercount=corp_data.memberCount,
            )
            return corp
        except Exception, e:
            print "Error: %s. On Corporation.create_corporation with id %d" \
                % (e, corp_id)
            return Corporation()
