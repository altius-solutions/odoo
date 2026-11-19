# Part of Altius ERP. See LICENSE file for full copyright and licensing details.
{
    'name': 'Altius Branding',
    'summary': 'White-label Odoo Community as Altius ERP',
    'description': """
Altius ERP branding for the Odoo Community web client.

Replaces user-visible Odoo marks (title, favicon, login, database manager,
navbar, user menu, settings blurb, and Enterprise upsells) with Altius
Solutions branding, and switches the backend palette to indigo.
    """,
    'category': 'Hidden',
    'version': '20.0.1.0.0',
    'author': 'Altius Solutions',
    'website': 'https://altiusol.com',
    'license': 'LGPL-3',
    'depends': [
        'web',
        'base_setup',
        'mysubscription',
    ],
    'auto_install': True,
    'post_init_hook': 'post_init_hook',
    'data': [
        'data/ir_config_parameter.xml',
        'views/webclient_templates.xml',
        'views/module_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            (
                'before',
                'web/static/src/scss/primary_variables.scss',
                'altius_branding/static/src/scss/primary_variables.scss',
            ),
            ('append', 'altius_branding/static/src/scss/brand_overrides.scss'),
        ],
        'web.assets_backend': [
            'altius_branding/static/src/scss/backend.scss',
            'altius_branding/static/src/js/user_menu.js',
            'altius_branding/static/src/js/title.js',
            'altius_branding/static/src/js/enterprise.js',
            'altius_branding/static/src/js/documentation.js',
            'altius_branding/static/src/xml/branding.xml',
        ],
        'web._assets_frontend_helpers': [
            (
                'after',
                'web/static/src/scss/bootstrap_overridden_frontend.scss',
                'altius_branding/static/src/scss/frontend_primary.scss',
            ),
        ],
        'web.assets_frontend': [
            'altius_branding/static/src/scss/login.scss',
        ],
    },
}
