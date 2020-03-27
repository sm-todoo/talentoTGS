from odoo import models,fields,api

class BenefitCenter(models.Model):
    _name='benefit.center'
    _description='This module will modify CRM'

    name=fields.Char('Centros de Beneficios')
    code=fields.Char('Code')
    bussines_units_id=fields.Many2one('business.units','Unidade de Negocio')
    segment_id=fields.Many2one('segment','Segmento')
