# -*- coding: utf-8 -*-
# from odoo import http


# class HrPayrollNew(http.Controller):
#     @http.route('/hr_payroll_new/hr_payroll_new/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_payroll_new/hr_payroll_new/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_payroll_new.listing', {
#             'root': '/hr_payroll_new/hr_payroll_new',
#             'objects': http.request.env['hr_payroll_new.hr_payroll_new'].search([]),
#         })

#     @http.route('/hr_payroll_new/hr_payroll_new/objects/<model("hr_payroll_new.hr_payroll_new"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_payroll_new.object', {
#             'object': obj
#         })
