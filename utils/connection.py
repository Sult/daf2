import urllib2
import os
import time
from collections import namedtuple

from django.db.models import get_model
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import eveapi

from django.core.cache import cache


#get data from cache
def get_cache(key):
    return cache.get(key)


#set data to cache
def set_cache(key, data, timeout):
    cache.set(key, data, timeout)


#create connection to eveapi. only allows x-requests per second
def api_connect():
    timestamp = int(time.time())
    if api_connect.timestamp == timestamp:
        api_connect.counter += 1
        if api_connect.counter == settings.EVE_API_REQUESTS:
        #if api_connect.counter == 10:
            time.sleep(1)
            api_connect.counter = 0
            api_connect.timestamp = timestamp
            print timestamp
    else:
        api_connect.timestamp = timestamp
        api_connect.counter = 0
    return eveapi.EVEAPIConnection()
api_connect.timestamp = int(time.time())
api_connect.counter = 0


#create an authenticated connection with the eveapi (personal data)
def auth_connect(api):
    result = api_connect().auth(keyID=api.key, vCode=api.vcode)
    return result


###### Non-Authenticated #######
# get public character information
def characterinfo(characterid):
    cache_key = "characterinfo_%d" % characterid
    result = get_cache(cache_key)
    if not result:
        cache_timer = 60 * 10
        api = api_connect()
        result = api.eve.CharacterInfo(characterId=characterid)
        set_cache(cache_key, result, cache_timer)
    return result


#get public corporation information
def corporationsheet(corporationid):
    cache_key = "corporationsheet_%d" % corporationid
    result = get_cache(cache_key)
    if not result:
        cache_timer = 60 * 10
        api = api_connect()
        result = api.corp.CorporationSheet(corporationID=corporationid)
        set_cache(cache_key, result, cache_timer)
    return result


# get current sovholder list
def sovereignty():
    cache_key = "sovereignty"
    result = get_cache(cache_key)
    if not result:
        cache_timer = 60 * 60
        api = api_connect()
        result = api.map.Sovereignty().solarSystems
        set_cache(cache_key, result, cache_timer)
    return result


#get list of all alliances
def alliancelist():
    cache_key = "alliancelist"
    result = get_cache(cache_key)
    if not result:
        cache_timer = 60 * 60
        api = api_connect()
        result = api.eve.AllianceList().alliances
        set_cache(cache_key, result, cache_timer)
    return result


# returns all corporations of an alliance by allianceid
def alliancecorporations(allianceid):
    """ returns a list of namedtuples that hold corporationid
     and startdate(timestamp) """

    api = api_connect()
    alliances = api.eve.AllianceList().alliances
    row = alliances.Get(allianceid, False)
    result = []
    if row and row.memberCount > 0:
        MemberCorporation = namedtuple(
            "MemberCorporation",
            "corporationid startdate"
        )
        for corp in row.memberCorporations:
            result.append(MemberCorporation(
                corporationid=corp.corporationID,
                startdate=corp.startDate)
            )
    return result


#get icon from eve image database
def icon_url(path, pk, size):
    """ Explination: https://image.eveonline.com/ """

    if path == "Character":
        filetype = "jpg"
    else:
        filetype = "png"
    return "http://image.eveonline.com/%s/%d_%d.%s" % \
        (path, pk, size, filetype)


# get icon model from object
def icon_model(obj):
    model_name = obj._meta.object_name
    model = get_model(obj._meta.app_label, model_name + "Icon")
    return model


#create or overwrite old icon
def update_icons(obj, pk, icon_type):
    model = icon_model(obj)
    sizes = model.icon_sizes()

    for s in sizes:
        url = icon_url(icon_type, pk, s)
        #create_or_overwrite_icon(model, obj, pk, s)

        temp, created = model.objects.get_or_create(
            relation=obj,
            typeid=pk,
            size=s,
        )
        #result = urllib.urlretrieve(url)
        #temp.icon.save(os.path.basename(url), File(open(result[0])))
        #temp.save()
        img = NamedTemporaryFile(delete=True)
        img.write(urllib2.urlopen(url).read())
        img.flush()
        temp.icon.save(os.path.basename(url), File(img))
        temp.save()


#### Authenticated (Account) #####
#Get ApiKeyInfo  https://neweden-dev.com/Account/APIKeyInfo
def apikeyinfo(api):
    cache_key = "apikeyinfo_%d" % api.pk
    result = get_cache(cache_key)
    if not result:
        cache_timer = 60
        auth = auth_connect(api)
        result = auth.account.APIKeyInfo().key
        set_cache(cache_key, result, cache_timer)
    return result


# get account information
def accountstatus(api):
    cache_key = "accountstatus_%d" % api.pk
    result = get_cache(cache_key)
    if not result:
        cache_timer = 60 * 5
        auth = auth_connect(api)
        result = auth.account.AccountStatus()
        set_cache(cache_key, result, cache_timer)
    return result


# get charactersheet
def charactersheet(character):
    cache_key = "charactersheet_%d" % character.pk
    result = get_cache(cache_key)
    if not result:
        cache_timer = 60 * 5
        auth = auth_connect(character.api)
        result = auth.char.CharacterSheet(
            characterID=character.characterid
        )
        set_cache(cache_key, result, cache_timer)
    return result


#characterinfo with api suplied
def characterinfo_api(character):
    cache_key = "characterinfo_api_%d" % character.pk
    result = get_cache(cache_key)
    if not result:
        cache_timer = 60 * 5
        auth = auth_connect(character.api)
        result = auth.eve.CharacterInfo(characterId=character.characterid)
        set_cache(cache_key, result, cache_timer)
    return result


#characterinfo with api suplied
def skillintraining(character):
    cache_key = "skillintraining_%d" % character.pk
    result = get_cache(cache_key)
    if not result:
        cache_timer = 60 * 2
        auth = auth_connect(character.api)
        result = auth.char.SkillInTraining(
            characterId=character.characterid
        )
        set_cache(cache_key, result, cache_timer)
    return result


#get character skillqueue
def skillqueue(character):
    cache_key = "skillqueue_%d" % character.pk
    result = get_cache(cache_key)
    if not result:
        cache_timer = 60 * 3
        auth = auth_connect(character.api)
        result = auth.char.SkillQueue(
            characterId=character.characterid
        ).skillqueue
        set_cache(cache_key, result, cache_timer)
    return result


def walletjournal(character):
    auth = auth_connect(character.api)
    result = auth.char.WalletJournal(
        characterID=character.characterid,
        rowCount=2500,
    ).transactions
    return result
