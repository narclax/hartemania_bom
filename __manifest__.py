# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'autor': 'Jose Marty',
    'name': 'Reportes Lista de Precios Hartemania',
    'category': 'Reports',
    'summary': 'Lista de Precios para Hartemania.',
    'description': """
Lista de Precios personalizados para Hartemania.
""",
    'depends': ['mrp'],
    'data': [
        
        'views/bom_report.xml',
        'views/pdf_line.xml',
        'views/bom_report_structure.xml',
    ],
    'demo': [
        #'data/website_demo.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OEEL-1',
    'assets': {
        'web.assets_frontend': [
            #'jm_henca_website/static/src/css/fonts/fonts.css',
            #'jm_henca_website/static/src/css/custom.css',
        ],
    }
}
