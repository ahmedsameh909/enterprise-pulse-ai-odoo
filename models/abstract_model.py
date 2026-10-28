from odoo import fields, models

# contains common fields for all models that are used in the enterprise pulse module

class EnterprisePulseAbstractModel(models.AbstractModel):
    _name = 'enterprisepulse.abstract.model'
    _description = 'Enterprise Pulse Shared Fields'

    source_record_id = fields.Char(string='Source Record ID', index=True, copy=False)
    source_dataset_id = fields.Many2one(
        'enterprisepulse.source.dataset',
        string='Source Dataset',
        ondelete='set null'
    )
