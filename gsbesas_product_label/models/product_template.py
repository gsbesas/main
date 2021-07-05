from odoo import api, fields, models, tools, _
from datetime import datetime, timedelta

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    exp_date = fields.Date(string='Exp Date', copy=False)
    contents = fields.Char('Contents')
    manufacture = fields.Char('Manufacturer')