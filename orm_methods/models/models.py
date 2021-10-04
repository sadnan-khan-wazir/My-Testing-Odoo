# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritResPartner(models.Model):
    _inherit = 'res.partner'

    total_text = fields.Char(string='Total Net')


class orm_methods(models.Model):
    _inherit = 'sale.order'

    name = fields.Char('Name')
    age = fields.Integer('Age')
    note = fields.Text('student Id')
    note_1 = fields.Text('students Record')


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    class_1 = fields.Char('Name')
    age = fields.Integer('Age')



class HrEmployee(models.Model):
    _inherit = 'hr.employee'


    trainer = fields.Char('Trainer')
    date_id = fields.Date('Open date')
    hr_id= fields.Selection([('manager','Manager'),('dircetor','Director'),('hr','Hr')] ,string='Job posstion')
    sal_id= fields.Integer('Salary')
    @api.onchange('department_id','hr_id')
    def _onchange_Hr_Emp(self):
        for x in self:
            if x.hr_id == 'manager':
                x.sal_id= 4000
            else:
                x.sal_id=3000



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    tax_pak= fields.Integer('Tax')







#             record.value2 = float(record.value) / 100
