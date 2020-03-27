from odoo import models,fields,api

class Competitors(models.Model):
    _name='competitors'
    _description='This module will modify CRM'

    name=fields.Char('Competidor')
    code=fields.Char('Code')
    weaknesses_id=fields.Many2one('weaknesses','DEBILIDADES')
    strengths_id=fields.Many2one('strengths','FORTALEZAS')
