from collections import OrderedDict
from datetime import datetime, timedelta

from django.db import models
from django.conf import settings
from django.utils.timezone import utc

from .skills import Skill, SkillGroup
from apps.bulk.models import Corporation
from config.storage import OverwriteStorage
from utils import connection
from utils.connection import set_cache, get_cache
from utils.common import convert_timestamp, icon_size_name, lookahead


class CharacterApi(models.Model):
    """ charactertype apis """

    api = models.ForeignKey("apies.Api")
    characterid = models.BigIntegerField()
    charactername = models.CharField(max_length=254)
    corporationid = models.BigIntegerField()
    corporationname = models.CharField(max_length=254)

    def __unicode__(self):
        return self.charactername

    #get right icon for characters view
    def characters_view_icon(self):
        try:
            icon = self.characterapiicon_set.get(size=128, relation=self)
            return icon.icon
        except CharacterApiIcon.DoesNotExist:
            return None

    #def character sheet image
    def characters_sheet_icon(self):
        try:
            icon = self.characterapiicon_set.get(size=200, relation=self)
            return icon.icon
        except CharacterApiIcon.DoesNotExist:
            return None

    #get the data for landing page after character selection
    def character_sheet(self):
        sheet = getattr(connection, "characterinfo_api")(self)
        employment = self.employment_history(sheet)
        return sheet, employment

    #employment history of a player
    @staticmethod
    def employment_history(sheet):
        cache_key = "employment_history_%d" % sheet.characterID
        result = get_cache(cache_key)
        if not result:
            cache_timer = 60 * 60
            result = []
            for corp_data in sheet.employmentHistory:
                result.append({
                    "corporation": Corporation.find_corporation(
                        corp_data.corporationID
                    ),
                    "startdate": convert_timestamp(
                        corp_data.startDate
                    )
                })
            set_cache(cache_key, result, cache_timer)
        return result

    #get skill in training
    def skill_in_training(self):
        training_skill = None
        if self.api.access_to("SkillInTraining"):
            in_training = getattr(connection, "skillintraining")(self)
            try:
                training_skill = {
                    "skill": Skill.objects.get(
                        typeid=in_training.trainingTypeID
                    ).typename,
                    "to_level": in_training.trainingToLevel,
                    "finnished": convert_timestamp(
                        in_training.trainingEndTime
                    )
                }
            except AttributeError:
                training_skill = {"skill": "No skill in training"}
        return training_skill

    #characters trained skills
    def trained_skills(self):
        cache_key = "trained_skills_%d" % self.pk
        result = get_cache(cache_key)
        if not result:
            cache_timer = 60 * 10
            sheet = getattr(connection, "charactersheet")(self)
            groups = SkillGroup.objects.exclude(
                groupname="Fake Skills"
            ).order_by("groupname")
            skills = Skill.objects.order_by("typename")
            all_skills = OrderedDict()
            skillpoints = {}

            for group in groups:
                all_skills[group.groupname] = list()
                skillpoints[group.groupname] = 0

            for skill in skills:
                trained = sheet.skills.Get(skill.typeid, False)
                if trained:
                    all_skills[skill.skillgroup.groupname].append(
                        {
                            "skill": skill,
                            "level": trained.level
                        }
                    )
                    skillpoints[skill.skillgroup.groupname] += \
                        trained.skillpoints

            result = {
                "all_skills": all_skills,
                "skillpoints": skillpoints,
            }

            set_cache(cache_key, result, cache_timer)
        return result

    #get skillqueue
    def skill_queue(self):
        queue = None
        if self.api.access_to("SkillQueue"):
            queue = {}
            skills = getattr(connection, "skillqueue")(self)
            queue["skills"] = skills
            queue["total"] = self.total_skillpoints(skills)
            now = datetime.now().replace(tzinfo=utc)
            trainingtime = convert_timestamp(
                skills[-1].endTime
            ) - now
            trainingtime -= timedelta(microseconds=trainingtime.microseconds)
            queue["trainingtime"] = trainingtime
        return queue

    #get total skillpoints for skills in queue
    @staticmethod
    def total_skillpoints(skills):
        total = 0
        for skill in skills:
            total += skill.endSP - skill.startSP
        return total

    #walletjournal (results can be increased and filtered)
    def wallet_journal(self):
        cache_key = "walletjournal_%d" % self.pk
        result = get_cache(cache_key)
        if not result:
            cache_timer = 60 * 5
            transactions = getattr(connection, "walletjournal")(self)
            result = list()
            for transaction in transactions:
                result.append(transaction)
            set_cache(cache_key, result, cache_timer)
        return result


class CharacterApiIcon(models.Model):
    """ images related to characters """

    relation = models.ForeignKey("characters.CharacterApi")
    size = models.IntegerField(choices=settings.IMAGE_SIZES)
    typeid = models.IntegerField()
    icon = models.ImageField(
        upload_to="images/characters/",
        storage=OverwriteStorage(),
        blank=True,
        null=True
    )

    class Meta:
        unique_together = ["size", "relation"]

    def __unicode__(self):
        return "Character Image %s" % icon_size_name(self.size)

    # def save(self, *args, **kwargs):
    #     try:
    #         temp = CharacterApiIcon.objects.get(pk=self.pk)
    #         if temp.icon != self.icon:
    #             temp.icon.delete()
    #     except ObjectDoesNotExist:
    #         pass
    #     super(CharacterApiIcon, self).save(*args, **kwargs)

    #get list of wanted character icon sizes
    @staticmethod
    def icon_sizes():
        return [32, 64, 128, 200, 256]
