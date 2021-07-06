import itertools
import logging

from odoo import api, fields, models, tools, _, SUPERUSER_ID
from odoo.exceptions import ValidationError, RedirectWarning, UserError
from odoo.osv import expression

_logger = logging.getLogger(__name__)


class ProductBrand(models.Model):
    _name = "product.brand"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _description = "Product Brand"
    _order = "name"
    
    
    name = fields.Char('Name', index=True, required=True, translate=True)
    company_id = fields.Many2one(
        'res.company', 'Company', index=1)
    phone = fields.Char('Phone')
    email = fields.Char('Email')
    