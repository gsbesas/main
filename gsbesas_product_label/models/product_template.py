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
            move_line = self.env['stock.move.line'].search(
                [('location_id.usage', '=', 'supplier'),('location_dest_id.usage', '=', 'internal')],
                order='date desc',
                limit=1
            )
            if move_line:
                record['exp_date'] = move_line.expiration_date