# -*- coding: utf-8 -*-
# from odoo import http


# class Custom-addons(http.Controller):
#     @http.route('/custom-addons/custom-addons/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom-addons/custom-addons/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom-addons.listing', {
#             'root': '/custom-addons/custom-addons',
#             'objects': http.request.env['custom-addons.custom-addons'].search([]),
#         })

#     @http.route('/custom-addons/custom-addons/objects/<model("custom-addons.custom-addons"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom-addons.object', {
#             'object': obj
#         })
