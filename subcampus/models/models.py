# -*- coding: utf-8 -*-

from odoo import models, fields, api


class subcampus(models.Model):
    _name = 'subcampus.subcampus'
    _description = 'subcampus.subcampus'
    _rec_name = 'name'

    name = fields.Char('school name')
    faculty = fields.Char('Faculty')
    address = fields.Char('Address')
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
