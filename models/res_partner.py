from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    segment = fields.Selection([
        ('retail', 'Retail'),
        ('wholesale', 'Wholesale'),
        ('vip', 'VIP'),
    ])
    _sql_constraints = [
        ('source_id_company_uniq',
         'unique(source_customer_id, company_id)',
         'Source customer ID must be unique per company.'),
    ]