import eveapi
from apps.apies.models import CallGroup, Call
from apps.characters.models import RefType

api = eveapi.EVEAPIConnection()
data = api.API.CallList()


def call_groups():
    for group in data.callGroups:
        try:
            CallGroup.objects.create(
                groupid=group.groupID,
                name=group.name,
                description=group.description,
            )
        except:
            print "You stupid"


def calls():
    for call in data.calls:
        if call.accessMask == 8388608:
            #no need for limited character info. Or full acces or none
            continue

        try:
            Call.objects.create(
                accessmask=call.accessMask,
                accounttype=call.type,
                name=call.name,
                callgroup=CallGroup.objects.get(groupid=call.groupID),
                description=call.description,
            )
        except:
            print "Some shit didnt work dude"


def reftypes():
    for ref in api.eve.RefTypes().refTypes:
        try:
            RefType.objects.create(
                reftypeid=ref.refTypeID,
                reftypename=ref.refTypeName,
            )
        except:
            "You fucked up mate"

call_groups()
calls()
reftypes()
