from odoo import models,fields,api

class Weaknesses(models.Model):
    _name='weaknesses'
    _description='This module will modify CRM'

    name=fields.Char('Debilidades')
    code = fields.Char('Code')