from odoo import api, fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    industry = fields.Char(string="Industry")
    description = fields.Char(string="Description")
    created_at = fields.Date(string="Created at")
    is_active = fields.Boolean(string="Is Active")