from odoo import api, models, fields
from odoo.exceptions import ValidationError

class Allocation(models.Model) :
    _name = 'materiel.allocation'
    _inherit = 'mail.thread'
    _description = 'Allocation des matériels'

    materiel_id = fields.Many2one('materiel', string='Matériel ID', required=True, tracking=True)
    motif = fields.Char(string='Motif', required=True, tracking=True)
    quantity = fields.Integer(string='Quantité', tracking=True)
    is_available = fields.Boolean(string='Disponible', tracking=True, readonly=True)
    
    @api.constrains('quantity', 'motif', 'is_available')
    def check_before_create(self) :
        for rec in self :
            materiel = self.env['materiel'].browse(rec.materiel_id.id).exists()
            if len(rec.motif) < 5 :
                raise ValidationError("Veuillez entrez un motif d'au moins 5 caractères")
            if rec.quantity <= 0 :
                raise ValidationError("Veuillez entrer une quantité valide")
                
            # Cette fonction est appelée aaprès celle de création.
            # Donc la valeur de l'available_quantity aura deja ete soustrait de la quantite
            # Donc on peut verifier si le reste est inferieur a 0 ou non
            available_quantity = materiel.available_quantity + self.quantity
            if available_quantity <= 0 :
                raise ValidationError("Matériel indisponible pour le moment")
            if rec.quantity > available_quantity :
                raise ValidationError("Quantité indisponible. Entrez une quantité inférieure !")        


    @api.onchange('quantity', 'materiel_id')
    def onchange_materiel(self) :
        materiel = self.env['materiel'].browse(self.materiel_id.id).exists()
        self.is_available = int(materiel.available_quantity) >= self.quantity

    @api.model
    def create(self, vals) :
        # Modification de la quantité disponible avant l'ajout dans la bdd
        materiel = self.env['materiel'].browse(vals['materiel_id']).exists()
        materiel.available_quantity = materiel.available_quantity - vals['quantity']
        return super(Allocation, self).create(vals)
    
    def action_allocation_remettre(self) :
        # Ajout de la quantite disponible avant la suppression de l'allocation
        materiel = self.env['materiel'].browse(self.materiel_id.id).exists()
        materiel.available_quantity = materiel.available_quantity + self.quantity
        self.unlink()
        return {'type': 'ir.actions.act_window_close'}
        