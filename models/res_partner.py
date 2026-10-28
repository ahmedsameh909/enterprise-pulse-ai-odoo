from odoo import fields, models

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner', 'enterprisepulse.abstract.model']

    segment = fields.Selection([
        ('consumer', 'Consumer'),
        ('corporate', 'Corporate'),
        ('home_office', 'Home Office'),
        ('other', 'Other')
    ], string='Customer Segment', help='Business-defined segment for AI/Analytics')

    _sql_constraints = [
        ('source_id_company_uniq',
         'unique(source_record_id, company_id)',
         'Source record ID must be unique per company.'),
    ]