from odoo import api, fields, models

class StockWarehouse(models.Model):
    _name = 'stock.warehouse'
    _inherit = ['stock.warehouse', 'enterprisepulse.abstract.model']

    location_type = fields.Char(string="Location Type")
    region = fields.Char(string="Region")

    country = fields.Char(string="Country")
    state = fields.Char(string="State")
    city = fields.Char(string="City")
    latitude = fields.Float(string="Latitude", digits=(10, 7))
    longitude = fields.Float(string="Longitude", digits=(10, 7))

    source_location_id = fields.Char(string="Source Location")
