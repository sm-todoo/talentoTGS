from odoo import models,fields,api

class UnspscCode(models.Model):
    _name='undpsc.code'
    _description='This module will modify CRM'

    name=fields.Char('Códigos UNSPSC')
    code = fields.Char('Code')