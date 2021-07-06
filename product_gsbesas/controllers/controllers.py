# -*- coding: utf-8 -*-
# from odoo import http


# class ProductGsbesas(http.Controller):
#     @http.route('/product_gsbesas/product_gsbesas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_gsbesas/product_gsbesas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_gsbesas.listing', {
#             'root': '/product_gsbesas/product_gsbesas',
#             'objects': http.request.env['product_gsbesas.product_gsbesas'].search([]),
#         })

#     @http.route('/product_gsbesas/product_gsbesas/objects/<model("product_gsbesas.product_gsbesas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_gsbesas.object', {
#             'object': obj
#         })
