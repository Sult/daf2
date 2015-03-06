from datetime import datetime

from django.conf import settings
from django.utils.timezone import utc


#converts a timestamp to a aware datetime object
def convert_timestamp(timestamp):
    try:
        temp = datetime.fromtimestamp(timestamp).replace(tzinfo=utc)
        return temp
    except TypeError:
        return None


#see if you reached last iteration of a forloop
def lookahead(iterable):
    it = iter(iterable)
    last = it.next()
    for val in it:
        yield last, False
        last = val
    yield last, True


##### ICONS #####
#Get the size name of an icon
def icon_size_name(size):
    for s in settings.IMAGE_SIZES:
        if s[1] == size:
            return s[0]
