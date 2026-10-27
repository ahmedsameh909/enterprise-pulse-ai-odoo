from odoo import fields, models, api

class product_template(models.Model):
    _inherit = 'product.template'

    level = fields.Integer(compute="_compute_hierarchical_level", string="Hierarchical Level")

    @api.depends('categ_id.parent_path')
    def _compute_hierarchical_level(self):
        for record in self:
            path = record.categ_id.parent_path or ''
            record.hierarchical_level = len([p for p in path.split('/') if p]) -1