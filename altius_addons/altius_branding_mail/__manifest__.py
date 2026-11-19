# Part of Altius ERP. See LICENSE file for full copyright and licensing details.
{
    'name': 'Altius Branding — Mail',
    'summary': 'Altius footer and colors on outgoing emails',
    'category': 'Hidden',
    'version': '20.0.1.0.0',
    'author': 'Altius Solutions',
    'website': 'https://altiusol.com',
    'license': 'LGPL-3',
    'depends': ['altius_branding', 'mail', 'mail_bot'],
    'auto_install': True,
    'post_init_hook': 'post_init_hook',
    'data': [
        'views/mail_templates.xml',
    ],
}
