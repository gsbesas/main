from odoo import api, fields, models, tools, _
from datetime import datetime, timedelta

class Picking(models.Model):
    _inherit = 'stock.picking'
    
    box_number = fields.Char('Box Number')
    barcode = fields.Char(
        'Barcode', copy=False,
        help="International Article Number used for product identification.")