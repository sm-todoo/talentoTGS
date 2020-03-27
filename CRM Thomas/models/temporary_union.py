from odoo import models,fields,api

class TemporaryUnion(models.Model):
    _name='temporary.union'
    _description='This module will modify CRM'

    name=fields.Char('Unión Temporal')
    code = fields.Char('Code')
