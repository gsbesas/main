from odoo import api, fields, models, tools, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    exp_date = fields.Datetime('Exp Date', compute='get_last_po_date')
    contents = fields.Char('Contents')
    manufacture = fields.Char('Manufacturer')
    
    def get_last_po_date(self):
        for record in self:
            product_ids = record.product_variant_ids and record.product_variant_ids.ids or []
            move_line = self.env['stock.move.line'].search(
                [('location_id.usage', '=', 'supplier'),
                ('location_dest_id.usage', '=', 'internal'),
                ('state', '!=', 'cancel'),('product_id', 'in', tuple(product_ids))],
                order='date desc',
                limit=1
            )
            exp_date = False
            if move_line:
                exp_date = move_line.expiration_date
            record.exp_date = exp_date