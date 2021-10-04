# -*- coding: utf-8 -*-

from odoo import models, fields, api



class InvoiceInheritPdf(models.Model):
    _inherit = 'res.partner'

    arabic_name = fields.Char(string='Arabic Name')
    arabic_address = fields.Char(string='Arabic Address')
    arabic_city = fields.Char(string='Arabic City')
    arabic_zip = fields.Char(string='Arabic Zip')
    arabic_c = fields.Char(string='Arabic Country')
    vat_c = fields.Char(string='Arabic Vat')



class ResCompanyInherit(models.Model):
    _inherit = 'res.company'

    arabic_name_c = fields.Char(string='Arabic Name')
    arabic_address_c = fields.Char(string='Arabic Address')
    arabic_city_c = fields.Char(string='Arabic City')
    arabic_c = fields.Char(string='Arabic Country')
    arabic_zip_c = fields.Char(string='Arabic Zip')
    arabic_z = fields.Char(string='Arabic Zip')
    chamber = fields.Char(string='Chamber')
