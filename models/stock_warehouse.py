from odoo import fields, models

class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    location_type = fields.Char(string="Location Type")
    region = fields.Char(string="Region")

    country = fields.Char(string="Country")
    state = fields.Char(string="State")
    city = fields.Char(string="City")
    latitude = fields.Float(string="Latitude")
    longitude = fields.Float(string="Longitude")

    source_location_id = fields.Char(string="Source Location")

    