{
    'name': 'Esis Logistique',
    "author": "Master Code",
    'application': True,
    "summary": "Réalisé dans le cadre de Hackaton",
    'depends': ['mail'],
    "data": [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/materiel/enregistrement.xml',
        'views/materiel/allocation.xml',
        'views/materiel/categorie.xml',
        'views/demande/need.xml',
        'views/demande/request.xml',
    ]
}