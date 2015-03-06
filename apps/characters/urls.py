from django.conf.urls import patterns, url

from apps.characters import views

urlpatterns = patterns(
    '',
    url(
        r'^characters/$',
        views.characters,
        name='characters',
    ),
    url(
        r'^characters/(?P<pk>\d+)/$',
        views.select_character,
        name='select_character',
    ),
    url(
        r'^characters/sheet/$',
        views.character_sheet,
        name='character_sheet',
    ),
    url(
        r'^character/skills/$',
        views.character_skills,
        name='character_skills'
    ),
    url(
        r'^character/journal/$',
        views.character_journal,
        name='character_journal',
    ),
)
