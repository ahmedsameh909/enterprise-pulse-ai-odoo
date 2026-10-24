from odoo import fields, models

class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    location_type = fields.Char(string="Location Type")
    region = fields.Char(string="Region")
    source_location_id = fields.Char(string="Source Location")
    