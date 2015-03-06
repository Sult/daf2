from datetime import datetime

from django.db import models
from django.utils.timezone import utc


class Sovereignty(models.Model):
    """ what solarsystems can change owners """

    solarsystemid = models.BigIntegerField(unique=True)
    solarsystemname = models.CharField(max_length=254, unique=True)

    def __unicode__(self):
        return self.solarsystemname


class SovereigntyHolder(models.Model):
    """ who holds the sovereignty of a system """

    now = datetime.now().replace(tzinfo=utc)
    sovereignty = models.ForeignKey("bulk.Sovereignty")
    last_refresh = models.DateTimeField(default=now)
    allianceid = models.BigIntegerField(null=True)
    corporationid = models.BigIntegerField(null=True)
    factionid = models.BigIntegerField(null=True)

    def __unicode__(self):
        return self.sovereignty.solarsystemname

    # check if the owner changed
    @staticmethod
    def owner_change(sov):
        system, created = Sovereignty.objects.get_or_create(
            solarsystemid=sov.solarSystemID,
            solarsystemname=sov.solarSystemName,
        )
        try:
            holder = SovereigntyHolder.objects.filter(
                sovereignty=system
            ).order_by("-last_refresh")[0]
            if holder.allianceid != sov.allianceID or \
                holder.factionid != sov.factionID or \
                    holder.corporationid != sov.corporationID:
                SovereigntyHolder.create_holder(sov, system)
        except IndexError:
            SovereigntyHolder.create_holder(sov, system)

    #crate new sovholder
    @staticmethod
    def create_holder(sov, system):
        try:
            SovereigntyHolder.objects.create(
                sovereignty=system,
                allianceid=sov.allianceID,
                corporationid=sov.corporationID,
                factionid=sov.factionID,
            )
        except:
            print """Error: SovereigntyHolder.create_holder failed for system:
             %s""" % system.solarsystemname
            pass
