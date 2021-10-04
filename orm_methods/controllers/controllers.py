# -*- coding: utf-8 -*-
# from odoo import http


# class OrmMethods(http.Controller):
#     @http.route('/orm_methods/orm_methods/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/orm_methods/orm_methods/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('orm_methods.listing', {
#             'root': '/orm_methods/orm_methods',
#             'objects': http.request.env['orm_methods.orm_methods'].search([]),
#         })

#     @http.route('/orm_methods/orm_methods/objects/<model("orm_methods.orm_methods"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('orm_methods.object', {
#             'object': obj
#         })
