from odoo import api, fields, models

class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    street = fields.Char()
    street2 = fields.Char()
    city = fields.Char()
    zip = fields.Char()
    country_id = fields.Many2one('res.country')
    state_id = fields.Many2one(
        'res.country.state',
        domain="[('country_id', '=?', country_id)]",
    )
    phone = fields.Char()