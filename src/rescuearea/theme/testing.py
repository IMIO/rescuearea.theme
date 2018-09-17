# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import rescuearea.theme


class RescueareaThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=rescuearea.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rescuearea.theme:default')


RESCUEAREA_THEME_FIXTURE = RescueareaThemeLayer()


RESCUEAREA_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(RESCUEAREA_THEME_FIXTURE,),
    name='RescueareaThemeLayer:IntegrationTesting'
)


RESCUEAREA_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(RESCUEAREA_THEME_FIXTURE,),
    name='RescueareaThemeLayer:FunctionalTesting'
)


RESCUEAREA_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        RESCUEAREA_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='RescueareaThemeLayer:AcceptanceTesting'
)
