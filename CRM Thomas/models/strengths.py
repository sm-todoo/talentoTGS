from odoo import models,fields,api

class Strengths(models.Model):
    _name='strengths'
    _description='This module will modify CRM'

    name=fields.Char('Fortalezas')
    code = fields.Char('Code')