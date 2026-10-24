from odoo import fields, models

class StockLocation(models.Model):
    _inherit = 'stock.location'

    source_location_id = fields.Char(index=True, copy=False)