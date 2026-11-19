# Part of Altius ERP. See LICENSE file for full copyright and licensing details.
{
    'name': 'Altius Branding — Portal',
    'summary': 'Altius footer on the customer portal',
    'category': 'Hidden',
    'version': '20.0.1.0.0',
    'author': 'Altius Solutions',
    'website': 'https://altiusol.com',
    'license': 'LGPL-3',
    'depends': ['altius_branding', 'portal'],
    'auto_install': True,
    'data': [
        'views/portal_templates.xml',
    ],
    'assets': {
        'portal.assets_chatter_style': [
            (
                'after',
                'portal/static/src/chatter/portal/scss/primary_variables.scss',
                'altius_branding_portal/static/src/scss/chatter.scss',
            ),
        ],
    },
}
