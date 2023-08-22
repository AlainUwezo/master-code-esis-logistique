from odoo import api, models, fields
from odoo.exceptions import ValidationError

class Materiel(models.Model) :
    _name = 'materiel'
    _description = 'Mateiriel'

    materiel_id = fields.Many2one('materiel', string='Matériel')
    num_serie = fields.Char(string='Numéro de série')
    name = fields.Char(string='Nom du matériel', required=True)
    quantity = fields.Integer(string='Quantité', required=True, tracking=True)
    categorie_id = fields.Many2one('materiel.categorie', string='Catégorie', required=True)
    available_quantity = fields.Integer(string='Quantité disponible', tracking=True)

    @api.constrains('quantity', 'name')
    def check_before_create(self) :
        for rec in self :
            if len(rec.name) < 5 :
                raise ValidationError("Veuillez entrez un nom d'au moins 5 caractères")
            if rec.quantity <= 0 :
                raise ValidationError("Veuillez entrer une quantité valide")

    @api.onchange('quantity')
    def onchange_quantity(self) :
        self.available_quantity = self.quantity

    def action_materiel_allouer(self) :
        return {
            'type': 'ir.actions.act_window',
            'name': 'Allouer matériel',
            'res_model': 'materiel.allocation',
            'view_mode': 'form',
            'context': {'default_materiel_id': self._origin.id},
            'target': 'new'
        }

    def action_materiel_delete(self) :
        self.unlink()
        return {'type': 'ir.actions.act_window_close'}

    @api.model_create_multi
    def create(self, vals_list) :
        for vals in vals_list :
            vals['num_serie'] = self.env['ir.sequence'].next_by_code('esis.logistique.materiel')
            vals_list['available_quantity'] = vals['quantity']
        return super(Materiel, self).create(vals_list)