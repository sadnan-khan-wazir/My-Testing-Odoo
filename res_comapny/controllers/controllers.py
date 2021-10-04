# -*- coding: utf-8 -*-
# from odoo import http


# class ResComapny(http.Controller):
#     @http.route('/res_comapny/res_comapny/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/res_comapny/res_comapny/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('res_comapny.listing', {
#             'root': '/res_comapny/res_comapny',
#             'objects': http.request.env['res_comapny.res_comapny'].search([]),
#         })

#     @http.route('/res_comapny/res_comapny/objects/<model("res_comapny.res_comapny"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('res_comapny.object', {
#             'object': obj
#         })
