# Part of Altius ERP. See LICENSE file for full copyright and licensing details.
{
    'name': 'Altius Branding — Website',
    'summary': 'Remove the Odoo website upsell from the public footer',
    'category': 'Hidden',
    'version': '20.0.1.0.0',
    'author': 'Altius Solutions',
    'website': 'https://altiusol.com',
    'license': 'LGPL-3',
    'depends': ['altius_branding', 'website'],
    'auto_install': True,
    'data': [
        'views/website_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'altius_branding_website/static/src/xml/website_loader.xml',
        ],
    },
}
