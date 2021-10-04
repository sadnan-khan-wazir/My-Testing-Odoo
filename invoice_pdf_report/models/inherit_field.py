# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Invoice_FieldInherit(models.Model):
    _inherit = 'account.move'

    invoice_no = fields.Integer(string='Invoice No')
    po_contract_no = fields.Integer(string='PO/Contract No')
    ref_date = fields.Date(string='Ref. Date')
    po_contract_date = fields.Date(string='Ref. Date')
    invoice_Type = fields.Char(string='Invoice Type')

