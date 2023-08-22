from odoo import api, fields, models

class Stock(models.Model) :
    _name = 'stock'
    _description = 'Stock'

    quantity = fields.Integer()
    unit_value = fields.Float()
