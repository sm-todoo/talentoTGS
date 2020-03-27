from odoo import models,fields,api

class BusinessUnits(models.Model):
    _name='business.units'
    _description='This module will modify CRM'

    name=fields.Char('Unidad de Negocio')
    code = fields.Char('Code')
    
