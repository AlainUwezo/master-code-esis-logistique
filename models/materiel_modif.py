from odoo import api, models, fields
from odoo.exceptions import ValidationError

class MaterielModification(models.Model) :
    _name = 'materiel.modifier'
    _description = 'Modification du matériel'

    materiel_id = fields.Many2one('materiel', string='Matériel ID', required=True)
    quantity = fields.Integer(string='quantity', required=True)
    action = fields.Selection([('1', "Ajouter"), ('2', "Retirer")], string="Action", required=True)

    @api.constrains('quantity')
    def check_before_create(self) :
        for rec in self :
            materiel = self.env['materiel'].browse(rec.materiel_id.id).exists()
            if rec.quantity <= 0 :
                raise ValidationError("Quantité invalide")
            if rec.quantity > materiel.available_quantity :
                raise ValidationError("Impossible de retirer cette quantité. Rassurez-vous que la quantité à retirer est disponible.")

    @api.model
    def create(self, vals) :
        materiel = self.env['materiel'].browse(vals['materiel_id']).exists()
        if(vals['action'] == '1') : 
            materiel.quantity += vals['quantity']
            materiel.available_quantity += vals['quantity']
        else :
            materiel.quantity -= vals['quantity']
            materiel.available_quantity -= vals['quantity']
        return super(MaterielModification, self).create(vals)