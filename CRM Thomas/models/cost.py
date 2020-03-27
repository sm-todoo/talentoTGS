from odoo import models,fields,api

class Cost(models.Model):
    _name='cost'
    _description='This module will modify CRM'

    name=fields.Char('Costo')
    code = fields.Char('Code')