# -*- coding: utf-8 -*-

from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.interface import Interface, implementer

from collective.volto.contactsblock.interfaces import (
    IContactsBlock,
    ICollectiveVoltoContactsblockLayer,
)


@adapter(Interface, ICollectiveVoltoContactsblockLayer)
@implementer(IContactsBlock)
class ContactsBlockControlpanel(RegistryConfigletPanel):
    schema = IContactsBlock
    configlet_id = "ContactsBlock"
    configlet_category_id = "Products"
    schema_prefix = None
