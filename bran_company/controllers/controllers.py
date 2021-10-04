# -*- coding: utf-8 -*-
# from odoo import http


# class BranCompany(http.Controller):
#     @http.route('/bran_company/bran_company/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bran_company/bran_company/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bran_company.listing', {
#             'root': '/bran_company/bran_company',
#             'objects': http.request.env['bran_company.bran_company'].search([]),
#         })

#     @http.route('/bran_company/bran_company/objects/<model("bran_company.bran_company"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bran_company.object', {
#             'object': obj
#         })
