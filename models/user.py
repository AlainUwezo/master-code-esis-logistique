from odoo import api, fields, models

class User(models.Model) :
    _name = 'user'
    _description = 'User'

    name = fields.Char(string='Nom', required=True)
    lastname = fields.Char(string='Post-nom', required=True)
    firstname = fields.Char(string='Prénom')
    email = fields.Char(string='Email', required=True)
    password = fields.Char(string='Password', required=True)
    job_title = fields.Char(string='Titre du travail')
    