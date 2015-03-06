import re

from django import forms
from utils.connection import api_connect

from apps.apies.models import Api
from utils.common import convert_timestamp

#from apps.characters.models import Character


class ApiForm(forms.Form):
    key_ID = forms.CharField(min_length=7, max_length=7, required=True)
    verification_code = forms.CharField(
        min_length=64,
        max_length=64,
        required=True
    )

    def clean_key_ID(self):
        data = self.cleaned_data['key_ID']
        try:
            int(data)
        except ValueError:
            raise forms.ValidationError("Should contain 7 numbers")
        return data

    def clean_verification_code(self):
        data = self.cleaned_data['verification_code']
        if not re.match("^[A-Za-z0-9]*$", data):
            raise forms.ValidationError(
                "Should only contain 64 letters and numbers"
            )
        return data

    def clean(self):
        key = self.cleaned_data['key_ID']
        vcode = self.cleaned_data['verification_code']

        # if Api.objects.filter(key=key, vcode=vcode, active=True).exists():
        #     raise forms.ValidationError(
        #         "This key has already been entered, try to update it"
        #     )

        #connect with api and validate key
        api = api_connect()
        auth = api.auth(keyID=key, vCode=vcode)
        try:
            keyinfo = auth.account.APIKeyInfo()
        except RuntimeError:
            raise forms.ValidationError("Invallid data, cannot connect to api")

    def save(self, user):
        key = self.cleaned_data['key_ID']
        vcode = self.cleaned_data['verification_code']

        #connect with api and validate key
        api = api_connect()
        auth = api.auth(keyID=key, vCode=vcode)
        info = auth.account.APIKeyInfo()

        api = Api.objects.create(
            user=user,
            key=key,
            vcode=vcode,
            accounttype=unicode(info.key.type),
            expires=convert_timestamp(info.key.expires),
            accessmask=info.key.accessMask,

        )

        ##create related data tables
        api.create_related()

#https://github.com/ntt/eveapi/blob/master/apitest.py
#http://wiki.eve-id.net/APIv2_Page_Index#Character
