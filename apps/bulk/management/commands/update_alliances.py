import time
from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings

from apps.bulk.models import AllianceBulk
from utils import connection
from utils.common import convert_timestamp


#TODO: Make options to set custom sleep timer
class Command(BaseCommand):
    """ Create infinate loop that refreshes the AlianceBulk objects """

    #TODO: Add option for custom sleeptimer
    option_list = BaseCommand.option_list + (
        make_option(
            "--timer",
            action="store",
            type="int",
            dest="timer",
            default=settings.ALLIANCE_REFRESH,
            help="""Timer (in hours) before running refreshing again.
             Default sleeper is 1 day."""),
    )

    #handle is what actualy will be executed
    def handle(self, *args, **options):
        alliances = getattr(connection, "alliancelist")()

        #set timer before running again
        time.sleep(int(options['timer'])*60*60)
