from odoo import api, fields, models, tools, _
from datetime import datetime, timedelta
from odoo.tools import float_is_zero, float_compare

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    eu_asin = fields.Char('EU ASIN')
    us_asin = fields.Char('US ASIN')
    cogs_usd = fields.Float('CoGS (USD)', default=0.0)
    fnsku_usa_barcode = fields.Char('FNSKU USA Barcode')
    french_ingredients = fields.Char('French Ingredients')
    english_ingredients = fields.Char('English Ingredients')
    allergens = fields.Char('Allergens')
    
    product_brand_id = fields.Many2one(
        'product.brand', 'Brand Name & Manufacturer')