# -*- coding: utf-8 -*-
# from odoo import http


# class Subcampus(http.Controller):
#     @http.route('/subcampus/subcampus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/subcampus/subcampus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('subcampus.listing', {
#             'root': '/subcampus/subcampus',
#             'objects': http.request.env['subcampus.subcampus'].search([]),
#         })

#     @http.route('/subcampus/subcampus/objects/<model("subcampus.subcampus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('subcampus.object', {
#             'object': obj
#         })
