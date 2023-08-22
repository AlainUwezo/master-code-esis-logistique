from odoo import api, fields, models

class Consumable(models.Model) : 
    _name = 'consumable'
    _description = 'Consommable'

    name = fields.Char(string='Consommable', required=True)
    description = fields.Char(string='Description')
    consumable_type = fields.Char(string='Type')
    