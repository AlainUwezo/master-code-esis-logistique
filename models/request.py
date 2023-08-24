from odoo import api, fields, models

class Request(models.Model) :
    _name = 'request'
    _description = 'Requêtes'

    name = fields.Float(string="Liste des champs")
    state_request = fields.Boolean(string='Etat de requête')
    needs = fields.Many2one('needs', string='Objet du besoin')
    object = fields.Float(string="Objet")
    quantity = fields.Float(string="Prix unitaire")
    unit_price = fields.Float(string="Prix unitaire")
    total_price = fields.Float(string="Prix total")

    @api.model
    def init(self) :
        needs = self.env['needs'].search([])
        for i in needs :
            print("\n\n" + i.reference + "\n\n")

    def action_request_valider(self) :
        active_id = self.env.context.get('active_id')
        if active_id :
            record = self.env['needs'].browse(active_id)
            print("\n\n\n" + str(record.need_object) + "\n\n\n")
