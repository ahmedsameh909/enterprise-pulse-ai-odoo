from odoo import fields, models

class ProductCategory(models.Model):
    _inherit = "product.category"

    description = fields.Char(string="Description")
    source_category_code = fields.Char(string="Source Category Code")