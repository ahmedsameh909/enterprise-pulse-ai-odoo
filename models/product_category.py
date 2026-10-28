from odoo import fields, models

class ProductCategory(models.Model):
    _name = 'product.category'
    _inherit = ['product.category', 'enterprisepulse.abstract.model']

    description = fields.Char(string="Description")
    source_category_code = fields.Char(string="Source Category Code")