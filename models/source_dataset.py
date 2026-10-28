from odoo import fields, models

#this model is used to store the source dataset information for the enterprise pulse AI module foe each company
class EnterprisePulseSourceDataset(models.Model):
    _name = 'enterprisepulse.source.dataset'
    _description = 'Enterprise Pulse Source Dataset'

    name = fields.Char(required=True)
    description = fields.Text()
