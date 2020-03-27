from odoo import models,fields,api

class Segment(models.Model):
    _name='segment'
    _description='This module will modify CRM'

    name=fields.Char('Nombre del Segmento')
    code = fields.Char('Code')
