# -*- coding: utf-8 -*-

from odoo import models, fields, api


class testing(models.Model):
    _name = 'testing.testing'
    _description = 'testing.testing'
    _rec_name = 'address'

    name = fields.Char('Name')
    f_name = fields.Char('Father Name')
    contact = fields.Char('Phone')
    address = fields.Many2one('hostel.hostel')