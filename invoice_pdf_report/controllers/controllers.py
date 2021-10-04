# -*- coding: utf-8 -*-
# from odoo import http


# class InvoicePdfReport(http.Controller):
#     @http.route('/invoice_pdf_report/invoice_pdf_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_pdf_report/invoice_pdf_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_pdf_report.listing', {
#             'root': '/invoice_pdf_report/invoice_pdf_report',
#             'objects': http.request.env['invoice_pdf_report.invoice_pdf_report'].search([]),
#         })

#     @http.route('/invoice_pdf_report/invoice_pdf_report/objects/<model("invoice_pdf_report.invoice_pdf_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_pdf_report.object', {
#             'object': obj
#         })
