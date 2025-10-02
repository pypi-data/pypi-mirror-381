# -*- coding: utf-8 -*-
import json

from plone import api
from plone.restapi.services import Service
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse

from collective.volto.contactsblock.interfaces import IContactsBlock


class PathSettingsFinder:
    def __init__(self, settings):
        # Ordiniamo i settings per lunghezza decrescente del rootPath
        self.settings = sorted(settings, key=lambda s: len(s["rootPath"]), reverse=True)

    def find(self, path):
        if not path.startswith("/"):
            path = "/" + path

        for setting in self.settings:
            root = setting["rootPath"]
            if path == root or path.startswith(root.rstrip("/") + "/") or root == "/":
                return setting
        return None


@implementer(IPublishTraverse)
class ContactsBlockGet(Service):
    def __init__(self, context, request):
        super(ContactsBlockGet, self).__init__(context, request)

    def reply(self):

        record = api.portal.get_registry_record(
            "contact_configuration", interface=IContactsBlock, default=""
        )
        if not record:
            return []
        record = json.loads(record)
        physical_path = "/".join(self.context.getPhysicalPath())
        portal_id = api.portal.get().getId()
        if physical_path.startswith("/" + portal_id):
            # remove site name from physical path
            physical_path = physical_path[len(portal_id) + 1 :]
        settings_finder = PathSettingsFinder(record)
        found_setting = settings_finder.find(physical_path)
        if not found_setting:
            return []
        return found_setting
