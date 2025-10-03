# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.restapi.controlpanels.interfaces import IControlpanel
from zope.schema import SourceText
from collective.volto.contactsblock import _
import json


class ICollectiveVoltoContactsblockLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IContactsBlock(IControlpanel):
    contact_configuration = SourceText(
        title=_("contacts_configuration_label", default="Contacts configuration"),
        description="",
        required=True,
        default=json.dumps([{"rootPath": "/", "items": []}]),
    )
