from odoo import api, fields, models

class Categorie(models.Model) : 
    _name = 'materiel.categorie'
    _description = 'Categorie des matériels'

    designation = fields.Char(string='Designation', required=True)

    def action_categorie_delete(self) :
        self.unlink()
        return {'type': 'ir.actions.act_window_close'}