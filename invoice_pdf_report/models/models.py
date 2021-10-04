# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    ref_date = fields.Date(string="Ref Date.", required=False, )
    subject_id = fields.Text(string="Subject", required=False, )
    intro_id = fields.Html(string="Introduction", required=False, )
    terms_con = fields.Html(string="Terms And Conditions", required=False, )
    childs_id = fields.Many2one(comodel_name="res.partner", string="Kind Attention", required=False, )
    re_id = fields.Char(string="Revision No.", required=False, )
    re_date = fields.Date(string="Revision Date.", required=False, )


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    rev_no = fields.Char(string="Revision No", required=False, )
    rev_date = fields.Date(string="Revision Date", required=False, )
    ref_date = fields.Date(string="Ref Date.", required=False, )

    b_subject = fields.Html(required=False, )
    b_introduction = fields.Html(required=False, )
    term_condition = fields.Html(required=False, )

    employee_id = fields.Many2one(comodel_name="hr.employee", string="Sales Man Employee", required=False, )
    childs_id = fields.Many2one(comodel_name="res.partner", string="Kind Attention", required=False, )
    sale_note = fields.Text(string="Subject", required=False, size=16)


#
# class InvoiceInheritPdf(models.Model):
#     _inherit = 'res.partner'
#
#     arabic_name = fields.Char(string='Arabic Name')
#     arabic_address = fields.Char(string='Arabic Address')
#     arabic_city = fields.Char(string='Arabic City')
#     arabic_zip = fields.Char(string='Arabic Zip')
#     arabic_c = fields.Char(string='Arabic Country')
#     vat_c = fields.Char(string='Arabic Vat')
#
#
#
# class ResCompanyInherit(models.Model):
#     _inherit = 'res.company'
#
#     arabic_name_c = fields.Char(string='Arabic Name')
#     arabic_address_c = fields.Char(string='Arabic Address')
#     arabic_city_c = fields.Char(string='Arabic City')
#     arabic_c = fields.Char(string='Arabic Country')
#     arabic_zip_c = fields.Char(string='Arabic Zip')
#     arabic_z = fields.Char(string='Arabic Zip')
#     chamber = fields.Char(string='Chamber')
# class Invoice_pdf(models.Model):
#     _inherit = 'account.move'
#
#     arabic_zip_padf = fields.Char(string='Arabic Zip')



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
