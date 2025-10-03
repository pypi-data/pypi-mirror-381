# -*- coding: utf-8 -*-
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import collective.volto.contactsblock


class CollectiveVoltoContactsblockLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.volto.contactsblock)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.volto.contactsblock:default")


COLLECTIVE_VOLTO_CONTACTSBLOCK_FIXTURE = CollectiveVoltoContactsblockLayer()


COLLECTIVE_VOLTO_CONTACTSBLOCK_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_VOLTO_CONTACTSBLOCK_FIXTURE,),
    name="CollectiveVoltoContactsblockLayer:IntegrationTesting",
)


COLLECTIVE_VOLTO_CONTACTSBLOCK_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_VOLTO_CONTACTSBLOCK_FIXTURE,),
    name="CollectiveVoltoContactsblockLayer:FunctionalTesting",
)
