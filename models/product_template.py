from odoo import models


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = ['product.template', 'enterprisepulse.abstract.model']
    _description = 'Product Template'
