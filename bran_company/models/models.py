# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResUserInherit(models.Model):
    _inherit = 'res.users'

    designiation_id = fields.Char(string="Designation", required=False, )
