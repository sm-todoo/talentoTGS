# -*- coding: utf-8 -*-
#BY: ING.LUIS FELIPE PATERNINA VITAL - TODOO SAS.

from odoo import fields,models,api
import re
from odoo.exceptions import ValidationError


alphabet = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F'),
    ('G', 'G'),
    ('H', 'H'),
    ('I', 'I'),
    ('J', 'J'),
    ('K', 'K'),
    ('L', 'L'),
    ('M', 'M'),
    ('N', 'N'),
    ('Ñ', 'Ñ'),
    ('O', 'O'),
    ('P', 'P'),
    ('Q', 'Q'),
    ('R', 'R'),
    ('S', 'S'),
    ('T', 'T'),
    ('U', 'U'),
    ('V', 'V'),
    ('W', 'W'),
    ('X', 'X'),
    ('Y', 'Y'),
    ('Z', 'Z')
]


dire = [
    ('BIS', 'BIS'),
    ('BISSUR', 'BISSUR'),
    ('BISNORTE', 'BISNORTE'),
    ('BISOESTE', 'BISOESTE'),
    ('SUR', 'SUR'),
    ('NORTE', 'NORTE')   
]


av = [
    ('AV', 'AV'),
    ('CL', 'CL'),
    ('CR', 'CR'),
    ('TRANS', 'TRANS'),
    ('DIAG', 'DIAG'),
    ('AUT', 'AUT')   
]

class Todoo(models.Model):
    _inherit = 'hr.applicant'
    
    name1 = fields.Char(string="Primer Apellido")
    name2 = fields.Char(string="Segundo Apellido")
    name3 = fields.Char(string="Primer Nombre")
    name4 = fields.Char(string="Segundo Nombre")
    tratamiento = fields.Selection([('DRA.', 'DRA.'),('SRA.', 'SRA.'),('SRTA.', 'SRTA.'), ('ING.', 'ING.')])
    name5 = fields.Many2one('res.country')
    nit = fields.Char(string='NIT', size=11)
    #Campos de Dirección...
    field_1 = fields.Selection(av)
    field_2 = fields.Integer(required=True)
    field_3 = fields.Selection(alphabet)
    field_4 = fields.Selection(dire)
    field_5 = fields.Integer(required=True)
    field_6 = fields.Selection(alphabet)
    field_7 = fields.Selection(dire)
    field_8 = fields.Integer(required=True)
    field_9 = fields.Selection(dire)
    field_10 = fields.Char()
    field_11 = fields.Char()
    field_12 = fields.Char()
    street = fields.Char()
    field_12 = fields.Char()
   


    name13 = fields.Char(string="Nombre Completo")
    

     
    @api.constrains('nit')
    def _check_nit_size(self):
        pattern = "^\+?[0-9]*$"
        for record in self:
            if record.nit and re.match(pattern, record.nit) is None:
                raise ValidationError(("NIT debe ser numerico"))

    

    @api.onchange('field_1', 'field_2', 'field_3', 'field_4', 'field_5',
                  'field_6', 'field_7', 'field_8', 'field_9', 'field_10',
                  'field_11', 'field_12')
    def _onchange_street(self):
        self.street = "%s %s  %s %s %s %s %s %s %s %s %s %s" % (
            self.field_1 if self.field_1 else "",
            str(self.field_2),
            str(self.field_3 if self.field_3 else ""),
            self.field_4 if self.field_4 else "",
            str(self.field_5),
            str(self.field_6 if self.field_6 else ""),
            self.field_7 if self.field_7 else "",
            str(self.field_8),
            self.field_9 if self.field_9 else "",
            str(self.field_10 if self.field_10 else ""),
            self.field_11 if self.field_11 else "",
            self.field_12 if self.field_12 else "")