from odoo import api, fields, models

class Request(models.Model) :
    _name = 'request'
    _description = 'Requêtes'

    state_request = fields.Boolean(string='Etat de requête')
    need_ids = fields.Many2one('needs', string='Objet du besoin')
    
    @api.model
    def my_method(self) :
        need_obj = self.env['needs']
        needs = need_obj.search([])
        self.need_ids = [(6, 0, needs.ids)]
