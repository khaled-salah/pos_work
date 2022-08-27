# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    has_pos_show_logo = fields.Boolean(compute='compute_has_pos_show_logo', store=True)
    has_edit_partner_pos = fields.Boolean('Edit POS Partner', store=True)

    @api.depends('groups_id')
    def compute_has_pos_show_logo(self):
        if self.env.user.has_group('pos_contact_update.group_pos_logo_receipt_show'):
            self.has_pos_show_logo = True
