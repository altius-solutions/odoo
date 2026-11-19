# Part of Altius ERP. See LICENSE file for full copyright and licensing details.
{
    'name': 'Altius Branding — CRM',
    'summary': 'Hide CRM lead-generation upsells that point at Odoo IAP',
    'category': 'Hidden',
    'version': '20.0.1.0.0',
    'author': 'Altius Solutions',
    'website': 'https://altiusol.com',
    'license': 'LGPL-3',
    'depends': ['altius_branding', 'crm'],
    'auto_install': True,
    'assets': {
        'web.assets_backend': [
            'altius_branding_crm/static/src/lead_generation.js',
        ],
    },
}
