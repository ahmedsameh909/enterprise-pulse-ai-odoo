from odoo import fields, models

class StockLocation(models.Model):
    _inherit = 'stock.location'

    warehouse_city = fields.Char(related='warehouse_id.city', string='City')
    warehouse_country_id = fields.Many2one(related='warehouse_id.country_id', string='Country')