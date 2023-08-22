from odoo import api, fields, models

class Delivery(models.Model) : 
    _name = 'delivery'
    _description = 'Livraison'

    motif = fields.Char(string='Motif', required=True)
    quantity = fields.Integer(string='Quantité', required=True)