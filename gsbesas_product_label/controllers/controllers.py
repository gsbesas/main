# -*- coding: utf-8 -*-
# from odoo import http


# class GsbesasProductLable(http.Controller):
#     @http.route('/gsbesas_product_lable/gsbesas_product_lable/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gsbesas_product_lable/gsbesas_product_lable/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gsbesas_product_lable.listing', {
#             'root': '/gsbesas_product_lable/gsbesas_product_lable',
#             'objects': http.request.env['gsbesas_product_lable.gsbesas_product_lable'].search([]),
#         })

#     @http.route('/gsbesas_product_lable/gsbesas_product_lable/objects/<model("gsbesas_product_lable.gsbesas_product_lable"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gsbesas_product_lable.object', {
#             'object': obj
#         })
