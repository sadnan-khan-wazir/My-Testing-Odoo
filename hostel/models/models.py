# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class hostel(models.Model):
    _name = 'hostel.hostel'
    _description = 'hostel.hostel'
    _rec_name = 'address'

    state = fields.Selection([
        ('update','Update'),
        ('string','String'),
        ('new','New'),
    ],string='State')
    name = fields.Char('Hostel Name')
    s_info = fields.Char('Student information')
    s_name = fields.Char('Student Name')
    s_contact = fields.Char('Student Contact')
    admin = fields.Char('Admin Name')
    address = fields.Char('Hostel Address')
    reg = fields.Integer('Registration No')

    test = fields.Many2one('testing.testing', string="Test")


