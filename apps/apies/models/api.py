from django.db import models, IntegrityError
from django.db.models import get_model
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from .accessmask import Call
from utils.common import convert_timestamp, lookahead
from utils import connection


class Api(models.Model):
    """ charactertype apis """

    CHARACTER = "Character"
    ACCOUNT = "Account"
    CORPORATION = "Corporation"
    ACCOUNTTYPES = (
        (CHARACTER, "Character"),
        (ACCOUNT, "Account"),
        (CORPORATION, "Corporation"),
    )

    active = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    key = models.IntegerField(verbose_name="Key ID")
    vcode = models.CharField(max_length=254, verbose_name="Verification Code")
    accounttype = models.CharField(max_length=254, choices=ACCOUNTTYPES)
    expires = models.DateTimeField(null=True)
    accessmask = models.IntegerField()

    def __unicode__(self):
        return "Api from %s" % self.user.username

    #update api and remake related models
    def update(self):
        #update api fields
        key = getattr(connection, "apikeyinfo")(self)
        self.accounttype = key.type
        self.expires = convert_timestamp(key.expires)
        self.accessmask = key.accessMask
        self.save()

        #delete and recreate related character/corp models
        self.delete_related()
        self.create_related()

    #delete related api models
    def delete_related(self):
        #delete related corporation
        if self.accounttype == Api.CORPORATION:
            try:
                self.corporationapi.delete()
            except ObjectDoesNotExist:
                pass
        #delete related characters
        else:
            chars = self.characterapi_set.all()
            chars.delete()

    #create related api objects
    def create_related(self):
        if self.accounttype == Api.CORPORATION:
            self.create_corporation()
        else:
            self.create_characters()

    #create onetoone Corporation object
    def create_corporation(self):
        info = getattr(connection, "apikeyinfo")(self)
        for corp in info.characters:
            try:
                get_model("corporations", "CorporationApi").objects.create(
                    api=self,
                    corporationid=corp.corporationID,
                    corporationname=corp.corporationName,
                )
            except IntegrityError:
                print "Api tries to create more than 1 Corporation object"

    #create related Character objects (1 or 3)
    def create_characters(self):
        info = getattr(connection, "apikeyinfo")(self)
        for char in info.characters:
            new = get_model("characters", "CharacterApi").objects.create(
                api=self,
                characterid=char.characterID,
                charactername=char.characterName,
                corporationid=char.corporationID,
                corporationname=char.corporationName,
            )

            getattr(connection, 'update_icons')(
                new,
                new.characterid,
                "Character"
            )

    #create a name for the api
    def name(self):
        if self.accounttype == Api.CORPORATION:
            return self.corporationapi.corporationname
        else:
            string = ""
            for character, last in lookahead(self.characterapi_set.all()):
                string += character.charactername
                if not last:
                    string += " - "
            return string

    #string for GET use in templates
    def pk_string(self):
        return str(self.pk)

    #make expires a readable time in template
    def show_expires(self):
        if self.expires is None:
            return "Never"
        elif self.expires > timezone.now():
            return self.expires
        else:
            return "Expired!"

    #returns dict of all parts the api has access to
    def access(self):
        if self.accounttype == Api.CORPORATION:
            fields = Call.objects.filter(accounttype=Api.CORPORATION)
        else:
            fields = Call.objects.filter(accounttype=Api.CHARACTER)

        access_dict = {}
        for field in fields:
                access_dict[field.name] = bool(
                    field.accessmask & self.accessmask
                )

        return access_dict

    #check if you have acces to somthing by accesmask
    def access_to(self, name):
        if self.accounttype == Api.CORPORATION:
            call = Call.objects.get(accounttype=Api.CORPORATION, name=name)
        else:
            call = Call.objects.get(accounttype=Api.CHARACTER, name=name)
        return bool(call.accessmask & self.accessmask)

    #some simple account information
    def account_status(self):
        if self.access_to("AccountStatus"):
            info = getattr(connection, "accountstatus")(self)
            return info
        return None
