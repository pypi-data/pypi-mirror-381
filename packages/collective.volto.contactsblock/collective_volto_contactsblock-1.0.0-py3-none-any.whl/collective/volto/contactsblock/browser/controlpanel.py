# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from collective.volto.contactsblock.interfaces import IContactsBlock
from collective.volto.contactsblock import _


class ContactsBlocksForm(controlpanel.RegistryEditForm):

    schema = IContactsBlock
    label = _("contacts_block_settings_label", default="Contacts Block Settings")
    description = _(
        "contacts_blocks_settings_description", default="Manage contacts blocks."
    )


class ContactsBlocks(controlpanel.ControlPanelFormWrapper):
    form = ContactsBlocksForm
