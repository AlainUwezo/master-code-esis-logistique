from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Need(models.Model) :
    _name = 'needs'
    _description = 'Etat de besoin'

    need_object = fields.Text(string='Objet du besoin', required=True)
    imputation = fields.Char(string='Imputation')
    description = fields.Char(string='Description')
    reference = fields.Char(string='Référence')
    quantity = fields.Integer(string='Quantité', required=True)
    unit_price = fields.Float(string='Prix unitaire', required=True, tracking=True)
    total_price = fields.Float(string='Prix total', readonly=True, tracking=True)
    state_request = fields.Boolean(string='Validé')

    @api.constrains('need_object', 'quantity', 'unit_price')
    def check_before_create(self) :
         for rec in self :
            if len(rec.need_object) < 5 :
                raise ValidationError("Veuillez entrez un motif d'au moins 5 caractères")
            if rec.quantity <= 0 :
                raise ValidationError("Veuillez entrez une quantité valide")
            if rec.unit_price <= 0 :
                raise ValidationError("Veuillez entrez un prix unitaire valide")
                
    @api.onchange('unit_price', 'quantity')
    def onchange_materiel(self) :
        self.total_price = self.unit_price * self.quantity

    def action_need_delete(self) :
        self.unlink()
        return {'type': 'ir.actions.act_window_close'}
    
    
    @api.model_create_multi
    def create(self, vals_list) :
        for vals in vals_list :
            vals['reference'] = self.env['ir.sequence'].next_by_code('esis.logistique.besoin')
            vals['total_price'] = vals['unit_price'] * vals['quantity']
        return super(Need, self).create(vals_list)